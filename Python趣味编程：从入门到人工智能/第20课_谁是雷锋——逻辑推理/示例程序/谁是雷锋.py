'''
程序：谁是雷锋，逻辑推理
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
def main():
    '''求解谁是雷锋问题'''
    f = 1
    while f <= 4:
        p1 = f != 3
        p2 = f == 4
        p3 = f == 2
        p4 = f != 4
        if p1 + p2 + p3 + p4 == 1:
            print(f)
            break
        else:
            f += 1

if __name__ == '__main__':
    main()
