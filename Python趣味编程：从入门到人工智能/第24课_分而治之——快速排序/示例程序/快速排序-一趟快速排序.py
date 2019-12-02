'''
程序：一趟交换排序，用于实现快速排序算法
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
def partition(a, left, right):
    '''一趟交换排序'''
    base = left
    while left < right:
        while a[right] >= a[base] and left < right:
            right = right - 1
        while a[left] <= a[base] and left < right:
            left = left + 1
        a[left], a[right] = a[right], a[left]
    a[base], a[left] = a[left], a[base]
    return left
    
if __name__ == '__main__':
    a = [7, 5, 11, 2, 3]
    base = partition(a, 0, 4)
    print(base, a)

    #a = [7, 5, 11, 2, 3]
    #base = partition(a, 0, 4)
    #print(base, a)
    #base = partition(a, 0, 2)
    #print(base, a)
    #base = partition(a, 1, 2)
    #print(base, a)
