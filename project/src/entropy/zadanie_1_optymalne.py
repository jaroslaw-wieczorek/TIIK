from scipy import stats
import math
from collections import Counter

filename = "data/document_1.txt"


def H_old(s):
    probabilities = [n_x / len(s) for x, n_x in Counter(s).items()]
    e_x = [-p_x * math.log(p_x, 2) for p_x in probabilities]
    return sum(e_x)


def H(s):
    dictionary = Counter(s)
    return dictionary, stats.entropy([x for x in dictionary.values()], base=2)



with open(filename, "r") as file:
    text = file.read()
    print(H(text))
    print(H_old(text))
