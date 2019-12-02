'''
程序：手动实现选择排序算法
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
a = [7, 11, 3, 2, 5]
j = 0
p = j
i = j + 1
while i < len(a):
    if a[i] < a[p]:
        p = i
    i = i + 1
if p != j:
    a[j], a[p] = a[p], a[j]
print(a)
