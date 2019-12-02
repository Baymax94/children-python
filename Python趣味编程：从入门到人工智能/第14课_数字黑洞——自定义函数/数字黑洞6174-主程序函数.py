'''
程序：实现主程序模块，并创建两个桩函数
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

提示：采用“自顶向下，逐步求精”的思想编写程序
'''
#主程序
def main():
    n = input('请输入4位数字不完全相同的整数:')
    if check(n):
        blackhole(n)
    else:
        print('输入的整数不合法')

#检测数字
def check(n):
    return True

#黑洞变换
def blackhole(n):
    print(n)

#程序入口
if __name__ == '__main__':
    main()
