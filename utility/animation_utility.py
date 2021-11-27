import numpy as np
from matplotlib import pyplot as plt
from  matplotlib.animation import FuncAnimation
import utility.io_utility as io


def animate(filename, index):   
    global anim 
    
    # Reading File: ---------------------------------------------------------
    
    data = io.read(filename)
    
    # Plot: -----------------------------------------------------------------
    fig = plt.figure()
    plot = plt.imshow(data[0,:,:,index],  vmin=0, vmax=1)
    
        
    def init():
        plot.set_data(data[0,:,:,index])
        return [plot]
        
    def update(j):
        plot.set_data(data[j,:,:,index])
        return [plot]
        
    anim = FuncAnimation(fig, update,  frames=data[:,0,0,0].size, init_func = init, interval = 50, blit=True)
    #plt.axis("off")
