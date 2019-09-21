import matplotlib.pyplot as plt
x = [1, 3, 5, 7, 9, 11]
y = [4, 1, 5, 7, 10, 5]

plt.scatter(x, y, label="scatter", s=25, marker="o")

plt.xlabel('X-axis')
plt.ylabel("Y-axis")
plt.title('test Graph')
plt.legend()
plt.show()

# 散点图
