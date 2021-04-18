import MeCab
from collections import defaultdict

def create_mapping_list(line):
    out = []

    for elem in line.split("\n"):
        if not elem:
            continue

        surface, info = elem.split("\t")
        detail = info.split(",")      
        d = {
            "surface": surface,
            "base": detail[6],
            "pos": detail[0],
            "pos1": detail[1]
        }

        out.append(d)

    return out

def main():
    with open("neko.txt.mecab", "r") as f:
        res = f.read().split("EOS\n")
    
    out = list(map(create_mapping_list, res))

    freq = defaultdict(int)
    for line in out:
        for d in line:
            freq[d["surface"]] += 1
        
    print(sorted([(v, k) for k, v in freq.items()], reverse=True))


if __name__ == '__main__':
    main()
    