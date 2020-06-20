import matplotlib.pyplot as plt
import tensorflow as tf
%matplotlib inline

model =tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation ='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(7, activation='softmax')
])

checkpoint_path=r'C:\Users\arora\OneDrive\Documents\train_checkpoint\cp.ckpt' # change path to file in training data
model.load_weights(checkpoint_path)

# sample labels
labels=['assam handicrafts','assam silks','Bronze handicraft tamilnaidu','jute art west bengal','naga shawls assam','paintings west bengal','Singing bowls assam']

import numpy as np
from tensorflow.keras.preprocessing import image
# path = input()
# path =uploaded
path=r"C:\Users\arora\OneDrive\Desktop\12.jpg" # image url------------------------------------------
img= image.load_img(path,target_size=(150,150))
x= image.img_to_array(img)
x=np.expand_dims(x, axis=0)

images=np.vstack([x])
classes=model.predict(images, batch_size=10)
cout=0
for i in range(6):
    if classes[0][i]>classes[0][i+1]:
        classes[0][i+1]=classes[0][i]
    else:
        cout+=1
print(labels[cout])
