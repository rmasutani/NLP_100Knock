import re
import pandas as pd


df = pd.read_json('../data/jawiki-country.json', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]
for section in re.findall(r'(=+)([^=]+)\1\n', uk_text):

    print(section[0], section[1], section)


    # print(f'{section[1].strip()}\t{len(section[0]) - 1}')