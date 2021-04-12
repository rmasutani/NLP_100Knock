import sys

def cipher(s):
    if s.isalpha() and s.islower():
        return str(219 - ord(s))

    return s

def decipher(s):
    return

def main():
    s = "This is 3000 it."

    print("".join(map(cipher, s)))

if __name__ == '__main__':
    main()
    
