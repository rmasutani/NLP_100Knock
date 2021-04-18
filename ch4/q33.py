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
        for i in range(1, len(line)-1):
            if line[i]['surface'] == 'の' and\
                line[i-1]['pos'] == '名詞' and line[i+1]['pos'] == '名詞':
                combs.append((line[i-1]['surface'], line[i]['surface'], line[i+1]['surface']))
    
    print(combs)



if __name__ == '__main__':
    main()
    