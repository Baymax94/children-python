import keras
from keras import layers
import matplotlib.pyplot as plt
import keras.datasets.mnist as mnist
import numpy as np

print(train_image.shape)
print(train_label[0])

model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(64, activation='relu'))

model.add(layers.Dense(10, activation='softmax'))

model.compile(optimize='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['acc'])

model.fit(train_image, train_label, epochs=200, batch_size=512)
