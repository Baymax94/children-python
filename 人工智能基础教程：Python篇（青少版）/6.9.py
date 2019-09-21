from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3]
y = [1, 2, 3]
z = [2, 2, 2]

dx = [1, 2, 3]
dy = [1, 1, 1]
dz = [1, 1, 3]

ax1.bar3d(x, y, z, dx, dy, dz)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()

# 3D条形图
