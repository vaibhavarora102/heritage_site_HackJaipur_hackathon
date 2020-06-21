#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
import tensorflow as tf
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run():
    ''' '''

    

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



    checkpoint_path=r'cp.ckpt'
    model.load_weights(checkpoint_path)


    # sample labels
    labels=['assam handicrafts','assam silks','Bronze handicraft tamilnaidu','jute art west bengal','naga shawls assam','paintings west bengal','Singing bowls assam']

    import numpy as np
    from tensorflow.keras.preprocessing import image
    # path = input()
    # path =uploaded
    path= os.path.join(BASE_DIR, 'media/ml')+'/image.jpg'
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
    labels=['Handicrafts','Silks','Bronze Handicraft','Jute art','Naga Shawls','Paintings','Singing Bowls']
    return labels[cout]



