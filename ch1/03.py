import sys

def main():
    s = sys.stdin.readline()
    s = s.replace(",", " ,")
    s = s.replace(".", " .")
    s = s.split()
    
    print(list(map(len, s)))

if __name__ == '__main__':
    main()
    