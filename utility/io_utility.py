# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 19:05:16 2021

@author: sebas
"""
import numpy as np


def read(path):
    # open the file in read binary mode
    file = open(path, "rb")
    #read the file to numpy array
    data = np.load(file)
    
    return(data)



def write(data, path):
    # open a binary file in write mode
    file = open(path, "wb")
    # save array to the file
    np.save(file, data)
    # close the file
    file.close