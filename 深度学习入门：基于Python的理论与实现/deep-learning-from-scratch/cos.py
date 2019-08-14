# cos函数
# 使用pyplot的添加标题和x轴标签名等其他功能
import numpy as np
import matplotlib.pyplot as plt

# 生成数据
# 以0.1为单位，生成0到6的数据
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图形
plt.plot(x, y1, label="sin")
# 用虚线绘制
plt.plot(x, y2, linestyle="--", label="cos")
# x轴标签
plt.xlabel("x")
# y轴标签
plt.ylabel("y")
# 标题
plt.title('sin & cos')
plt.legend()
plt.show()
