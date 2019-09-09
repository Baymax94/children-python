#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import brown

# import chunker as chunker
# from text_chunker import chunker


# 无法解决模块问题
# 参考https://blog.csdn.net/qq_34494334/article/details/79362015
# 将输入的文本分块，每一块含有N个单词
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


input_data = ' '.join(brown.words()[:5600])
chunk_size = 900
text_chunks = chunker(input_data, chunk_size)

chunks = []
for count, chunk in enumerate(text_chunks):
    d = {'index': count, 'text': chunk}
    chunks.append(d)

count_vectorizer = CountVectorizer(min_df=7, max_df=18)
document_term_matrix = count_vectorizer.fit_transform(
    [chunk['text'] for chunk in chunks])

vocabulary = np.array(count_vectorizer.get_feature_names())

chunk_names = []
for i in range(len(text_chunks)):
    chunk_names.append('Chunk ' + str(i + 1))

print("\nDocument Term Matrix:")
formatted_text = '{:>9}' * (len(chunk_names) + 1)
print('\n', formatted_text.format('Word', *chunk_names), '\n', '*' * 76)
for word, item in zip(vocabulary, document_term_matrix.T):
    output = [word] + [str(freq) for freq in item.data]
    print(formatted_text.format(*output))

# 使用词袋模型提取词频矩阵
