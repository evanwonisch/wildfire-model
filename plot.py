# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 19:53:52 2021

@author: sebas
"""

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import utility.io_utility as io

result = io.read("data/result_output")
total_values = np.sum(result, axis = (1,2))


def plot_intensity():
    x = np.arange(result[:,0,0,0].size) / 24
    y = total_values[:,1]
    
    
    plt.plot(x, y, "C0", label = "Model")
    
    
    plt.xlabel("Zeit in Tagen")
    plt.ylabel("Gesamtbrandintensität")
    plt.legend()
    plt.grid()
    
def plot_speed():
    x = np.arange(result[:,0,0,0].size) / 24
    y = total_values[:,1]
    
    
    der = np.diff(y) / np.diff(x)
    x2 = (x[:-1] + x[1:]) / 2
    plt.plot(x2, der, 'r', label = "Model")
    
    
    plt.xlabel("Zeit in Tagen")
    plt.ylabel("Brandintensitätszunahme")
    plt.legend()
    plt.grid()
    
    
def plot_fuel():
    plt.plot(np.arange(result[:,0,0,0].size) / 24, total_values[:,0], "r", label = "Model")
    plt.xlabel("Zeit in Tagen")
    plt.ylabel("Gesamtbrennwert")
    plt.legend()
    plt.grid()