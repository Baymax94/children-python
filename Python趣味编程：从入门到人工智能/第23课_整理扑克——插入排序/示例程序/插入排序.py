'''
程序：插入排序算法
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
a = [7, 11, 3, 2, 5]
j = 1
while j < len(a):
    i = j
    while i > 0:
        if a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i = i - 1
        else:
            i = 0
    print(j, a)
    j = j + 1
