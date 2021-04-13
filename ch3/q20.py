import sys
import json 
from json import JSONDecoder

def read_england():
    path = "../data/jawiki-country.json"
    f = open(path)
    articles = (json.loads(o) for o in f.readlines())

    out = {}
    for d in articles:
        if d["title"] == "イギリス":
            out = d
            break
            
    return out["text"]

def main():
    path = "../data/jawiki-country.json"
    f = open(path)
    articles = (json.loads(o) for o in f.readlines())
    
    for d in articles:
        if d["title"] == "イギリス":
            print(d["text"])
            break

    return


if __name__ == '__main__':
    main()
    