'''
程序：用递归结构实现二分查找算法
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
def binary_search(n, a, left, right):
    '''二分查找(递归)'''
    if left <= right:
        mid = (right - left) // 2 + left
        print(left, right, mid)
        if n == a[mid]:
            return mid
        elif n < a[mid]:
            return binary_search(n, a, left, mid-1)
        else:
            return binary_search(n, a, mid+1, right)
    else:
        return -1

if __name__ == '__main__':
    '''程序入口'''
    a = [2, 3, 5, 7, 11, 13, 17, 19]
    pos = binary_search(17, a, 0, len(a)-1)
    print(pos)
