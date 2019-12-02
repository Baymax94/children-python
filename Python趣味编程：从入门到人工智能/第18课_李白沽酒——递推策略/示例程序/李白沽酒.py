'''
程序：李白沽酒，使用while循环
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
def main():
    '''求解李白沽酒问题'''
    n = 0
    i = 1
    while i <= 4:
        n = (n + 6) / 2
        i = i + 1
    print('瓶内原有酒%s升' % n)
    
if __name__ == '__main__':
    main()
