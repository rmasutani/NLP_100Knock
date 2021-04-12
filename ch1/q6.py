import sys
from q5 import letter_ngram

def main():
    # s1, s2 = input().rstrip().split()

    ng_1 = letter_ngram("paraparaparadise", 2)
    ng_2 = letter_ngram("paragraph", 2)

    print(ng_1 + ng_2)
    print()
    

if __name__ == '__main__':
    main()
    