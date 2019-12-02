'''
程序：区分旅客国籍，逻辑推理
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

用1~6分别为美国、德国、英国、法国、俄罗斯和意大利编号。
用枚举法列举6个人的国籍，判断如果已知条件成立，则找到答案。
提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def main():
    '''区分旅客国籍'''
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                for d in range(1, 7):
                    for e in range(1, 7):
                        f = 21 - a - b - c - d - e
                        if len({a, b, c, d, e, f}) == 6:
                            p1 = a == 3 or a == 6
                            p2 = b != 1 and b != 2
                            p3 = c == 3
                            p4 = e == 3 or e == 4 or e ==6
                            p5 = f != 2
                            if p1 + p2 + p3 + p4 + p5 == 5:
                                print(a, b, c, d, e, f)
                                return

if __name__ == '__main__':
    main()
