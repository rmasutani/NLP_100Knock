import re 
import pandas as pd 

df = pd.read_json('../data/jawiki-country.json', lines=True)
uk_text = df.query('title=="イギリス"')['text'].values[0]

