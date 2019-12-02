'''
程序：卡普雷卡尔黑洞，6174数字黑洞
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

提示：采用“自顶向下，逐步求精”的思想编写程序
'''
#主程序
def main():
    n = input('请输入4位不完全相同的整数:')
    if check(n):
        blackhole(n)
    else:
        print('输入的整数不合法')
 
#检测数字
def check(n):
    if not n.isnumeric():
        return False
    elif len(n) != 4:
        return False
    elif n == n[0] * 4:
        return False
    else:
        return True

#黑洞变换
def blackhole(n):
    print('变换过程:')
    while n != '6174':
        a = list(n)
        b = max_number(a)
        c = min_number(a)
        n = str(b - c)
        print('%s - %s = %s' % (b, c, n))
    print('变换结束！')

#取大数
def max_number(a):
    a.sort(reverse=True)
    num = int(''.join(a))
    return num

#取小数
def min_number(a):
    a.sort()
    num = int(''.join(a))
    return num

#程序入口
if __name__ == '__main__':
    main()
