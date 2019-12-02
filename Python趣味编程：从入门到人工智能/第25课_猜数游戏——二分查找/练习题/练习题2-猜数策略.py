'''
2.请完善程序，实现一个100以内的二分猜数游戏的提示猜数功能。
'''
left, right = 1, 100
while True:
    mid = (right - left) // 2 + left
    print('建议猜数:', mid)
    state = input('大了？小了？对了？(d/x/ok):')
    if state == 'ok':
        print('完成')
        break
    elif state == 'd':#大小
        right = mid - 1
    elif state == 'x':#小了
        left = mid + 1
