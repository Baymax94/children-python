#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

input_words = [
    'reading', 'calves', 'acting', 'undefined', 'house', 'possibly', 'version',
    'hotel', 'learned', 'experience'
]

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer('english')

stemmer_names = ['Porter', 'Lancaster', 'Snowball']
formatted_text = '{:>16}' * (len(stemmer_names) + 1)
print('\n', formatted_text.format('InputWord', *stemmer_names), '\n', '*' * 70)

for word in input_words:
    output = [
        word,
        porter.stem(word),
        lancaster.stem(word),
        snowball.stem(word)
    ]
    print(formatted_text.format(*output))

# 使用stemming 还原词汇
# porter lancaster snowball 算法
