import csv
import matplotlib.pyplot as plt

word = []
num = []
sum = 0
with open('E:/GitHub/children-python/人工智能基础教程：Python篇（青少版）/testresult.txt', 'r') as file:
    items = csv.reader(file, delimiter=' ')
    for item in items:
        word.append(item[0])
        re_num = (int(item[1]))
        num.append(int(re_num))
        sum = sum + int(re_num)
x = []
y = []

for i in range(10):
    x.append(word[i])
    y.append(num[i] / sum * 100)

plt.bar(x, y)
plt.xlabel('word')
plt.ylabel('probability (%)')
plt.show()

# 统计文件字符出现频率
