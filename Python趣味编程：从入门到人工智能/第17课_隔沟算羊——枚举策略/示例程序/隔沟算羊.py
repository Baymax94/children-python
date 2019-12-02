'''
程序：隔沟算羊，用枚举法求解方程问题
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
def main():
    '''求解隔沟算羊问题'''
    x = 1
    while True:
        y = x - 18
        if x + 9 == 2 * (y - 9):
            print(x, y)
            break
        else:
            x = x + 1

if __name__ == '__main__':
    main()
