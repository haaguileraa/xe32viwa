# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:53:46 2021

@author: User
"""


from distutils.core import setup
from setuptools import find_packages

setup(name='xe32viwa',
	  version='0.1',
	  author='DSSS',
	  author_email='katja.kossira@fau.de',
	  packages=find_packages(),
	  install_requirements=['numpy','Pillow','ipywidgets'])