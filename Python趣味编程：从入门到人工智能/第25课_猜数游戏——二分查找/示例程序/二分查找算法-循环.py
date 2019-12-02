'''
程序：用循环结构实现二分查找算法
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
def binary_search(n, a):
    '''二分查找(循环)'''
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (right - left) // 2 + left
        print(left, right, mid)
        if n == a[mid]:
            return mid
        elif n < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

if __name__ == '__main__':
    '''程序入口'''
    a = [2, 3, 5, 7, 11, 13, 17, 19]
    pos = binary_search(17, a)
    print(pos)
