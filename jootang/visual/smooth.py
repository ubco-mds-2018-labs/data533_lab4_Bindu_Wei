import numpy as np
import matplotlib.pyplot as plt

def smooth(y):
    list_x = list(range(0,len(y)))
    
    list_y = y
    plt.figure()
    poly = np.polyfit(list_x,list_y,5)
    poly_y = np.poly1d(poly)(list_x)
    plt.plot(list_x,poly_y)
    plt.plot(list_x,list_y)
    plt.show()
    
    
