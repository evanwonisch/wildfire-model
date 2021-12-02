# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 23:26:59 2021

@author: sebas
"""

import numpy as np
from matplotlib import pyplot as plt
from  matplotlib.animation import FuncAnimation
import utility.io_utility as io



def drawImage(field):
    plt.imshow(np.stack([field[:,:,1],field[:,:,0],np.zeros(shape = (field.shape[1], field.shape[2]))], axis = 2))

    
def animate(filename):   
    global anim 
    
    # Reading File: ---------------------------------------------------------
    
    data = io.read(filename)
    
    # Plot: -----------------------------------------------------------------
    fig = plt.figure()
    plot = drawImage(data[0,:,:,:])
    
        
    def init():
        plot.set_data(data[0,:,:,:])
        return [plot]
        
    def update(j):
        plot.set_data(data[j,:,:,:])
        return [plot]
        
    anim = FuncAnimation(fig, update,  frames=data[:,0,0,0].size, init_func = init, interval = 50, blit=True)
    #plt.axis("off")
