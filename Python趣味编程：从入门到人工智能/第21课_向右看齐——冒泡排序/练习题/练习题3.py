'''
3.请完善程序，在一轮排序过程中，如果没有发生元素交换，就提前结束整个排序过程。
'''
a = [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
j = 1
while j <= len(a) - 1:
    i = len(a) - 1
    swap = False
    while i >= j:
        if a[i] > a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            swap = True
        i = i - 1
    if not swap:
        break
    print(j, a)
    j = j + 1
