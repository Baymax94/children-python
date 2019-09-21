from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1, projection='3d')

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z1 = [-1, -2, -6, -3, -2, -7, -3, -3, -7, -2]
x2 = [-1, -3, -5, -7, -9, -11, -12, -15, -16, -17]
y2 = [4, 1, 5, 7, 10, 5, 12, 8, 9, 13]
z2 = [1, 2, 6, 3, 2, 7, 3, 3, 7, 2]

ax1.scatter(x1, y1, z1, color='b', marker='o')
ax1.scatter(x2, y2, z2, color='r', marker='x')
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()

# 3D散点图
