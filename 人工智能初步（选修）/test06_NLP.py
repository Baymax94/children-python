#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from nltk.corpus import brown


def chunker(input_data, N):
    input_words = input_data.split(' ')
    output = []
    cur_chunk = []
    count = 0
    for word in input_words:
        cur_chunk.append(word)
        count += 1
        if count == N:
            output.append(' '.join(cur_chunk))
            count, cur_chunk = 0, []
    output.append(' '.join(cur_chunk))
    return output


if __name__ == '__main__':
    input_data = ' '.join(brown.words()[:6300])
    chunk_size = 800
    chunks = chunker(input_data, chunk_size)
    print('\nNumber of text chunks =', len(chunks), '\n')
    for i, chunk in enumerate(chunks):
        print('Chunk', i + 1, '==>', chunk[:50])

# 文本分块
