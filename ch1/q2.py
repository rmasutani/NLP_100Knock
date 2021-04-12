import sys

def main():
    s1, s2 = input().rstrip().split()
    print("".join([x[0]+x[1] for x in zip(s1, s2)]))
    


if __name__ == '__main__':
    main()
    