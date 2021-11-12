# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:53:02 2021

@author: User
"""


import numpy as np
import pylab as plt
from ipywidgets import interact, fixed
from PIL import Image


newSize = (64,64)
imarray = np.random.rand(100,100,3) * 255
image = Image.fromarray(imarray.astype('uint8'))

def imshowResized(X, imgresize):
   
    resized = image.resize(imgresize, Image.ANTIALIAS)
    return resized



figure, (number1, number2) = plt.subplots(1,2)

number1.imshow(image)
number1.title.set_text("original image: ")
number2.imshow(imshowResized(image, newSize))
number2.title.set_text("resized image: ")


