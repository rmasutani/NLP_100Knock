import sys
import string 
import random



def main():
    sent = "I couldn't believe that I could actually understand what I was reading : the phoenomenal power of the human mind ."

    # one liner
    out = [word if len(word) <= 4 else word[0] + "".join(random.sample(word[1:-1], len(word)-2)) + word[-1] \
        for word in sent.split()]
    print(" ".join(out))

if __name__ == '__main__':
    s = "abcde"
    print(random.sample(s[1:-1], len(s)-2))

    main()

    
    