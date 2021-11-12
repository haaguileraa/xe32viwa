# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:53:02 2021

@author: User
"""


import numpy as np
import pylab as plt
from PIL import Image


def imshowResized(X, imgresize=None):
	
	
	if imgresize != None and len(imgresize) == 2:	
		resized = X.resize(imgresize, Image.ANTIALIAS)
	else:
		resized = X
	
	figure, (number1, number2) = plt.subplots(1,2)
	number1.imshow(X)
	number1.title.set_text("original image: ")
	number2.imshow(resized)
	number2.title.set_text("resized image: ")
	
	return resized


if __name__ == "__main__":
	newSize = (64,64)
	
	imarray = np.random.rand(100,100,3) * 255
	image = Image.fromarray(imarray.astype('uint8'))
	
	imshowResized(image, newSize)
	
