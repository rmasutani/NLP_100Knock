import sys
from q5 import letter_ngram

def main():
    # s1, s2 = input().rstrip().split()

    ng_1 = letter_ngram("paraparaparadise", 2)
    ng_2 = letter_ngram("paragraph", 2)

    print(ng_1 + ng_2) # Union
    print([(w1, w2) for w1 in ng_1 for w2 in ng_2]) # product

    print("se" in set(ng_1))
    print("se" in set(ng_2))
    

if __name__ == '__main__':
    main()
    