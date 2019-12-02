'''
3.请完善程序，实现对整数列表按升序排序。
'''
a = [5, 16, 8, 4, 2, 1]
for j in range(len(a)):
    p = j
    for i in range(j+1, len(a)):
        if a[i] < a[p]:
            p = i
    if p != j:
        a[j], a[p] = a[p], a[j]
    print(j+1, a)
