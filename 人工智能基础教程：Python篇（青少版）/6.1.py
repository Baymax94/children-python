import matplotlib.pyplot as plt

x1 = [1, 3, 4]
y1 = [2, 4, 1]
x2 = [1, 3, 4]
y2 = [4, 1, 5]

plt.plot(x1, y1, label='Line1')
plt.plot(x2, y2, label='Line2')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('test Graph')
plt.legend()
plt.show()

# 折线图
