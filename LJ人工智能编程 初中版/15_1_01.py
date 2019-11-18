import keras
from keras import layers
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('test.csv')
x = data.angle
y = data.speed

# 构建神经元模型
model = keras.Sequential()
model.add(layers.Dense(1, input_dim=1))

# 打印model.summary()查看模型的参数
print(model.summary())

# 编辑模型
model.compile(optimizer='adam', loss='mse')

# 训练模型
history = model.fit(x, y, batch_size=100, epochs=10000)

# 绘制数据
y_predict = model.predict(x)
plt.scatter(x, y)
plt.plot(x, y_predict, c='r')

# 缺少tensorflow环境
