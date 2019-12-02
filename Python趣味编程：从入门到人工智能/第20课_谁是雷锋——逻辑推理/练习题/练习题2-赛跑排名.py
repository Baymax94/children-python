'''
程序：赛跑排名，逻辑推理
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

使用枚举法列举6个小动物的排名，使用字典进行去重。
判断如果小猴、小狗、小兔说的话成立，则找到答案。
提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def main():
    '''赛跑排名'''
    for dog in range(1, 6):
        for rabbit in range(1, 6):
            for cat in range(1, 6):
                for monkey in range(1, 6):
                    for deer in range(1, 6):
                        if len({dog, rabbit, cat, monkey, deer}) == 5:
                            a = monkey < cat
                            b = deer < dog
                            c = rabbit < monkey and dog < rabbit
                            if a + b + c == 3:
                                print('小狗、小兔、小猫、小猴和小鹿的排名分别是：', end='')
                                print(dog, rabbit, cat, monkey, deer, sep=',')
                                return

if __name__ == '__main__':
    main()
