'''
程序：国王发金币
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def main():
    '''国王发金币'''
    coins, days, i = 0, 0, 0
    while True:
        i += 1
        for j in range(1, i + 1):
            coins += i
            days += 1
            if days == 365:
                print('骑士一共得到%d个金币' % coins)
                return
        
if __name__ == '__main__':    
    main()
