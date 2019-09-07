#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from nltk.stem import WordNetLemmatizer

input_words = [
    'reading', 'calves', 'acting', 'undefined', 'house', 'possibly', 'version',
    'hotel', 'learned', 'experience'
]

lemmatizer = WordNetLemmatizer()

lemmatizer_names = ['Noun Lemmatizer', 'Verb Lemmatizer']
formatted_text = '{:>24}' * (len(lemmatizer_names) + 1)
print('\n', formatted_text.format('InputWord', *lemmatizer_names), '\n',
      '*' * 74)

for word in input_words:
    output = [
        word,
        lemmatizer.lemmatize(word, pos='n'),
        lemmatizer.lemmatize(word, pos='v')
    ]
    print(formatted_text.format(*output))

# 使用lemmatization 还原词汇
