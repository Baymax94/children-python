'''
程序：冒泡排序算法
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
a = [11, 3, 5, 7, 2]
j = 1
while j <= len(a) - 1:
    i = len(a) - 1
    while i >= j:
        if a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
        i = i - 1
    print(j, a)
    j = j + 1
