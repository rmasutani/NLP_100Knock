import sys
import json
import re 

from q20 import read_england

def main():
    art = read_england()
    pattern = r"\[\[Category:.*\]\]"

    out = []
    for line in art.split("\n"):
        if re.match(pattern, line):
            out.append(line)

    print(out)

    return


if __name__ == '__main__':
    main()
    
