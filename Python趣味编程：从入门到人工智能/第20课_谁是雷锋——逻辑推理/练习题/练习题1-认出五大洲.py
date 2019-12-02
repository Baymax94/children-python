'''
程序：认出五大洲，逻辑推理
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

使用枚举法列举五大洲的编号，使用字典进行去重。
有5位同学每人都说了两句话，只要判断每个人有一句话是真的，就找到答案。
提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
def main():
    '''认出五大洲'''
    for asia in range(1, 6):
        for europe in range(1, 6):
            for africa in range(1, 6):
                for america in range(1, 6):
                    for oceania in range(1, 6):
                        if len({asia, europe, africa, america, oceania}) == 5:
                            a = (europe == 3) + (america == 2)
                            b = (asia == 4) + (oceania == 2)
                            c = (asia == 1) + (africa == 5)
                            d = (africa == 4) + (oceania == 3)
                            e = (europe == 2) + (america == 5)
                            if a == 1 and b == 1 and c == 1 and d == 1 and e == 1:
                                print('亚洲、欧洲、非洲、美洲和大洋洲的编号分别是：', end='')
                                print(asia, europe, africa, america, oceania, sep=',')
                                return
    
if __name__ == '__main__':
    main()
