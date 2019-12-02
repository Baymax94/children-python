'''
程序：环游地球，计算按福格路线环游地球的时间
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
# 输入数据
water_speed = input('请输入水路前进时速km/h:')
land_speed = input('请输入陆路前进时速km/s:')

# 处理数据
water_speed = int(water_speed)
land_speed = int(land_speed)
hours = 32000 / water_speed + 8000 / land_speed
days = round(hours / 24, 1)

# 输出数据
print('按福格路线环游地球要' + str(days) + '天')
