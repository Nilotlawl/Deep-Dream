import tensorflow as tf
import numpy as np

import matplotlib as mpl

import IPython.display as display
import PIL.Image

#test picture 
url = ''


#choosing model , lets choose googlenet for this 

base_model = tf.keras.applications.GoogLeNet(include_top=False, weights='imagenet')

#as googlenet is also based off inception net , same layers are present in it so can be modified

#Max activations of the layers named mixed3 and mixed 5

names = ['mixed3', 'mixed5']
layers = [base_model.get_layer(name).output for name in names']
          
# creating a feature extraction model named dream_model
dream_model = tf.keras.Model(inputs=base_model.input, outputs=layers)

#

class DeepDream(tf.module)
    def __init__(self, model):
    self.model = model

    @tf.function #what does this do?
    def __call__(self, img, step_size):
        
