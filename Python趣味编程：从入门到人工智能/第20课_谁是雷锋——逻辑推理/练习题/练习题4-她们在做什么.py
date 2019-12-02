'''
程序：她们在做什么，逻辑推理
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

用1~4为四人做的事情编号，即1是修指甲，2是写信，3是躺在床上，4是看书。
用枚举法列举四个人做的事情，用字典对四个人做的事情去重。
判断如果已知的5个条件成立，则找到答案。
提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def main():
    '''她们在做什么'''
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                for d in range(1, 5):
                    if len({a, b , c, d}) == 4:
                        p1 = a != 1 and a != 4
                        p2 = b != 1 and b != 3
                        p3 = (a == 3 and d == 1) or (a != 3 and d != 1)
                        p4 = c != 1 and c != 4
                        p5 = d != 3 and d != 4
                        if p1 + p2 + p3 + p4 + p5 == 5:
                            print(a, b, c, d)

if __name__ == '__main__':
    main()
