import re 
import pandas as pd 

df = pd.read_json('../data/jawiki-country.json', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]

out = {}

for section in re.findall(r'\|(.+?)\s=\s*(.+)', uk_text):
    print(section[0], "====", section[1])

    out[section[0]] = section[1]

print(out)