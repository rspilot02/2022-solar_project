from solar_objects import Star, Planet
import matplotlib.pyplot as plt
import pylab

def graphs(solar_objects):
    with open("statistic.txt", "r") as f:
        a = list(map(lambda x: x.rstrip().split(), f.readlines()))
    dat = a[-1]
    pylab.subplot(2, 1, 1)
    pylab.scatter([int(dat[0])], int(dat[-1]), color='black')
    
    pylab.subplot(2, 1, 2)
    pylab.scatter([int(dat[1])], int(dat[-1]), color='black')
    plt.show()
