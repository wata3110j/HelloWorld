import numpy as np
import matplotlib.pyplot as plt
import math
x=np.linspace(0,1,100)
plt.figure(0)
def y(a):
    return np.sin(2*a*math.pi)
plt.plot(x,y(x))
plt.show()
