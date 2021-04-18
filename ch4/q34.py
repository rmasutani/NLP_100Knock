import MeCab

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

    combs = []

    for line in out:
        count = 0
        for d in line:
            



if __name__ == '__main__':
    main()
    