import matplotlib.pyplot as plt
fig = plt.figure()
x = [1, 3, 5, 7, 9, 11, 15, 17]
y = [4, 1, 5, 7, 10, 5, 0, 20]
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 1, 2)
ax1.scatter(x, y)
ax1.set_title('scatter graph')
ax2.plot(x, y)
ax2.set_title('plot graph')
ax3.bar(x, y)
ax3.set_title('bar graph')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.annotate('first one', xy=(1, 1), xytext=(
    2, 2), arrowprops=dict(facecolor='r'))
plt.show()

# 子图
