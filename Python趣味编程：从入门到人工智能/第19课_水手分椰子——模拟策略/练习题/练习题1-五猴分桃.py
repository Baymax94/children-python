'''
程序：五猴分桃
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def allocate(n):
    '''模拟分桃'''
    for i in range(5):
        if (n - 1) % 5 != 0:
            return False
        else:
            n = (n - 1) / 5 * 4
    return True

def main():
    '''列举桃子数'''
    x = 0
    while not allocate(x):
        x = x + 1
    print('这堆桃子最少有%d个' % x)

if __name__ == '__main__':
    main()
