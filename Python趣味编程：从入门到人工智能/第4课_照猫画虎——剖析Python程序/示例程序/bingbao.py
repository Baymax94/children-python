# 验证冰雹猜想
def bingbao(n):
    arr.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        arr.append(n)
    return

if __name__ == '__main__':
    arr = []
    n = int(input('请输入一个正整数：'))
    bingbao(n)
    print(arr)
