'''
1.完善程序，将整数9插入到一个有序列表中，要求插入后的列表仍然有序。
'''
n = 9
a = [1, 2, 4, 5, 8, 16]
i = len(a)
a.append(n)
while i > 0:
    if a[i] < a[i-1]:
        a[i], a[i-1] = a[i-1], a[i]
        i = i - 1
    else:
        i = 0
print(a)
