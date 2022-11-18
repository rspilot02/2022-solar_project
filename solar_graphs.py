from solar_objects import Star, Planet
import matplotlib.pyplot as plt
import pylab
import numpy as np

def graphs():
    with open("stats.txt", "r") as f:
        a = list(map(lambda x: x.rstrip().split(), f.readlines()))
    dat = a[-1]
    pylab.subplot(3, 1, 1)
    pylab.scatter(np.array(float(dat[-1])), np.array(float(dat[0])), color='black')
    #name graph
    
    pylab.subplot(3, 1, 2)
    pylab.scatter(np.array(float(dat[-1])), np.array(float(dat[1])), color='black')
    
    pylab.subplot(3, 1, 3)
    pylab.scatter(np.array(float(dat[0])), np.array(float(dat[1])), color='black')
    
    plt.show()
