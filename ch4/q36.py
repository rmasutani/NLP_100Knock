from collections import defaultdict
from typing import ValuesView
import numpy as np 
import matplotlib.pyplot as plt 


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
        
    freq_list = sorted([(v, k) for k, v in freq.items()], reverse=True)

    values  = [f for f, v in freq_list[:10]]
    labels = [v for f, v in freq_list[:10]]

    x = np.arange(len(labels))
    width = 0.35
    fig, ax = plt.subplots()

    rect = ax.bar(x, values, width=width)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.show()

if __name__ == '__main__':
    main()
    