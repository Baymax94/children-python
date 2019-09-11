import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import layers

x = np.linspace(-1, 1, 100)
y = 2 * x**2 + 3 + np.random(100) * 0.5

model = keras.Sequential()
model.add(layers.Dense(units=10, input_dim=1, activation='relu'))
model.add(layers.Dense(units=20, activation='relu'))
model.add(layers.Dense(units=1, activation='relu'))
model.compile(optimizer=keras.optimizers.Adam(lr=0.1), loss='mse')
history = model.fit(x=x, y=y, batch_size=100, epochs=100)

y_predict = model.predict(x)
plt.scatter(x, y, c='b')
plt.plot(x, y_predict, c='r')
