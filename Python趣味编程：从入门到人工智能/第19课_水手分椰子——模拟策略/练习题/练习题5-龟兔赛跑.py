'''
程序：龟兔赛跑
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》

提示：该题的编程思路可参考《Scratch趣味编程进阶》中的相同问题。
'''
#初始化
tortoise = 0
rabbit = 0
sleep = 0
is_running = True
count = 1

#输入比赛时间
total = int(input('请输入龟兔赛跑的时间：'))

#计算龟兔赛跑的距离
while count <= total :
    # 乌龟一直在跑
    tortoise += 3
    # 处理兔子的情况
    if is_running :
        # 兔子在奔跑
        rabbit += 9
        # 每过10分钟就检查兔子是否超过乌龟
        if count % 10 == 0 and rabbit > tortoise :
                is_running = False
    else :
        # 兔子在睡觉
        sleep += 1
        # 睡过30分钟就让兔子继续奔跑
        if sleep == 30 :
            sleep = 0
            is_running = True
    # 比赛计时       
    count += 1
    
#输出兔子和乌龟的距离
print('兔子和乌龟跑过的距离分别是:', rabbit, tortoise)
