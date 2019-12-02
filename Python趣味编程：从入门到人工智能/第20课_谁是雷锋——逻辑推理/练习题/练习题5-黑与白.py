'''
程序：黑与白，逻辑推理
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

用0表示黑，1表示白。用枚举法列举5个人是黑是白。
判断如果ABCD四人说的成立，则找到答案。
提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def main():
    '''黑与白'''
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        p1 = (a == 1 and b + c + d + e == 3) or (a == 0 and b + c + d + e != 3)
                        p2 = (b == 1 and a + c + d + e == 0) or (b == 0 and a + c + d + e != 0)
                        p3 = (c == 1 and a + b + d + e == 1) or (c == 0 and a + b + d + e != 1)
                        p4 = (d == 1 and a + b + c + e == 4) or (d == 0 and a + b + c + e != 4)
                        if p1 + p2 + p3 + p4 == 4:
                            print(a, b, c, d, e)
                            return

if __name__ == '__main__':
    main()
