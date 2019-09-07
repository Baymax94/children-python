# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer

input_text = "Do you know what natural language processing is? This is a very interesting technology! We'll look at it in this section."

print("\nSentence tokenizer:")
print(sent_tokenize(input_text))

print("\nWord tokenizer:")
print(word_tokenize(input_text))

print("\nWord punct tokenizer:")
print(WordPunctTokenizer().tokenize(input_text))

# 文本分词
