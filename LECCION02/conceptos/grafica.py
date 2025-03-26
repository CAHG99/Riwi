import matplotlib.pyplot as pl
import numpy as np

t = np.linspace(0, 2* np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

pl.plot(x, y, 'r')
pl.fill(x,y,'r', alpha = 0.6)
pl.title("TIERRO", fontsize=40)
pl.axis('equal'),
pl.axis('off')
pl.text(-12.5,-2,"Te amo",fontsize=50, color="white", fontweight = 'bold', fontstyle = 'italic')
pl.show()
 