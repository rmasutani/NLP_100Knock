import sys
import re 
import json

from q20 import read_england


def main():
    art = read_england()
    pattern = r"\[\[Category:(.*)\]\]"

    out = []
    for line in art.split("\n"):
        res = re.search(pattern, line)

        if res:
            print(res.group(1))
            

    # print(out)

    return


if __name__ == '__main__':
    main()
    