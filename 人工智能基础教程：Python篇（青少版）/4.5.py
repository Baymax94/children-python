# 最大次数的单词
max_value=0
words={'T':4,'He':5,'let':9,'be':2,'what':3,'how':2,'the':7}
for item in words.items():
    if item[1]>max_value:
        max_value=item[1]
        word=item[0]

print("The most appeared word is : {}".format(word))