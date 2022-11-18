from solar_objects import Star, Planet
import matplotlib.pyplot as plt
import pylab
import numpy as np

def graphs():
    """
    Rendering the graphs with data from stats.txt
    r(t)
    v(t)
    v(r)
    """
    with open("stats.txt", "r") as f:
        a = list(map(lambda x: x.rstrip().split(), f.readlines()))
    v = []
    r = []
    t = []
    for s in a:
        v.append(float(s[1]))
        r.append(float(s[0]))
        t.append(float(s[2]))
        
    v = np.array(v)
    r = np.array(r)
    t = np.array(t)
        
    pylab.subplot(3, 1, 1)
    pylab.plot(t, r, color='black')
    pylab.title(r'$r(t)$')
    
    pylab.subplot(3, 1, 2)
    pylab.plot(t, v, color='black')
    pylab.title(r'$v(t)$')
    
    pylab.subplot(3, 1, 3)
    pylab.plot(r, v, color='black')
    pylab.title(r'$v(r)$')
    
    plt.show()
