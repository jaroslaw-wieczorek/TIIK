"""Counting letters and entropy."""
# -*- coding:utf-8 -*-
import math
from scipy import stats
from collections import Counter

filename = "data/document_1.txt"


def H(s):
    probabilities = [n_x / len(s) for x, n_x in Counter(s).items()]
    e_x = [-p_x * math.log(p_x, 2) for p_x in probabilities]
    return sum(e_x)


def describe(text: str="data/document_1.txt") -> dict:
    """Describe text in file."""
    dictionary = Counter(text)
    print("\n\n\n", dictionary)
    return dictionary


with open(filename, "r") as file:
    text = file.read()
    dictionary = describe(text)
    summary = sum(dictionary.values())
    print(len(dictionary))
    print("\nSum of symbols:", summary)
    for key in dictionary.keys():
        print(key, "=", dictionary[key], "  ", dictionary[key]/len(text))

    print(H("aaaabbcd"))
    print('\nEntropy:', H(text))
    print(stats.entropy([x for x in dictionary.values()], base=2))
