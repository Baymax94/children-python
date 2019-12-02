'''
1.请完善程序，实现一个100以内的二分猜数游戏。
'''
import random
n = random.randint(1, 100)
while True:
    guess = int(input('请输入一个整数:'))
    if guess == n:
        print('猜对了')
        break
    if guess > n:
        print('大了')
    else:
        print('小了')
