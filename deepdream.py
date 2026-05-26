import tensorflow as tf
import numpy as np

import matplotlib as mpl

import IPython.display as display
import PIL.Image

#test picture 
url = ''

class DeepDream(tf.module)
    def __init__(self, model):
    self.model = model

    @tf.function #what does this do?
    def __call__(self, img, step_size):
        
