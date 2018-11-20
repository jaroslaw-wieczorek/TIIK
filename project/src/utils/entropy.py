from scipy import stats
from collections import Counter

filename = "data/document_1.txt"

def H(s):
    dictionary = Counter(s)
    return dictionary, stats.entropy([x for x in dictionary.values()], base=2)


def main():
    with open(filename, "r") as file:
        text = file.read()
        print(H(text))


if __name__ == '__main__':
    main()
