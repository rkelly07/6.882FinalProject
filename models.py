# File for creating different models for the required experiments
# All models are based on pretrained versions of ResNet50
# Code referenced from tutorial at (https://www.tensorflow.org/tutorials/images/transfer_learning)

from __future__ import absolute_import, division, print_function

import os

import tensorflow as tf
from tensorflow import keras

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_size = 224

IMG_SHAPE = (image_size, image_size, 3)

def vision_only():
    # Create the base model from the pre-trained model ResNet50
    base_model = tf.keras.applications.ResNet50(input_shape=IMG_SHAPE,
                                                include_top=False, 
                                                weights='imagenet')
    model = tf.keras.Sequential([
        base_model,
        keras.layers.GlobalAveragePooling2D(),
        keras.layers.Dense(1, activation='sigmoid')
        ])

