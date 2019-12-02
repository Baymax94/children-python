'''
程序：利滚利债
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
def main():
    '''利滚利债'''
    x = 0
    for i in range(3):
        x = (x + 5) / 2
    print('向债主借的%s升粮食' % x)
    
if __name__ == '__main__':
    main()
