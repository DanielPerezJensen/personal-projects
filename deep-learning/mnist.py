import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.utils import plot_model

# 28*28 images of hand-written digits 0-9
mnist_data = tf.keras.datasets.mnist

# splits mnist data into training and testing data
(x_train, y_train), (x_test, y_test) = mnist_data.load_data()

# normalizes data for easier training
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

# constructing our model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

model.save('mnist.model')
# HOW TO LOAD MODEL
model = tf.keras.models.load_model('mnist.model')

# shows and predicts what number some drawn digit is
predictions = model.predict([x_test])
for i in range(12):
    print(np.argmax(predictions[i]))
    plt.imshow(x_test[i])
    plt.show()
