import sys

def main():
    s = input()
    
    ans = ""
    
    for i in range(1, len(s)):
        if i % 2 != 0:
            ans += s[i]
    
    print(ans)


if __name__ == "__main__":
    main()
