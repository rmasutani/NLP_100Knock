import sys
from q5 import split_word

def main():
    sent = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    firsts = set([1, 5, 6, 7, 8, 9, 15, 16, 19])
    words = split_word(sent)

    out = {}

    for i in range(len(words)):
        if i in firsts:
            out[i] = words[i][0]
            continue

        out[i] = words[i][0:2]
    
    print(out)


if __name__ == '__main__':
    main()
    
