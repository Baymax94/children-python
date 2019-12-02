'''
程序：水手分椰子，用模拟法求解数学问题
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
def allocate(n):
    '''模拟分椰子'''
    for i in range(3):
        n = (n - 1) / 3 * 2
    return (n - 1) % 3 == 0

def main():
    '''列举椰子数'''
    x = 4
    while not allocate(x):
        x = x + 1
    print(x)

if __name__ == '__main__':
    main()
