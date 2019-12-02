'''
3.请完善程序，实现对整数列表按升序排序。
'''
a = [5, 16, 8, 4, 12, 1]
for j in range(1, len(a)):
    i = j
    while i > 0:
        if a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i = i - 1
        else:
            i = 0
    print(j, a)
