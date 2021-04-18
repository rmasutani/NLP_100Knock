import re 
import pandas as pd 

df = pd.read_json('../data/jawiki-country.json', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]

out = {}
pattern_emp = r"'{3,}(.+?)'{3,}"
for section in re.findall(r'\|(.+?)\s=\s*(.+)', uk_text):
    # 強調を取り除く
    if re.search(pattern_emp, section[1]):
        print(section[1])
    out[section[0]] = section[1]

# print(out)