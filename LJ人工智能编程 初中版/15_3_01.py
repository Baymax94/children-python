import pandas as pd
import keras
from keras import layers
import numpy as np

# 读取信息资料
data = pd.read_csv('train.csv')
print(data.head())

y = data.Survived
x = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]

model = keras.Sequential()
model.add(layers.Dense(256, input_dim=11, activation='relu'))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(x, y, epochs=300)
