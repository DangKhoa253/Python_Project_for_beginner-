import numpy as np 
import matplotlib.pyplot as plot

x=np.arange(-2*np.pi,2*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)

plot.plot(x,y,x,z)
plot.xlabel(" x values from -2pi to 2pi")
plot.ylabel(" sinx and cosx")
plot.title("Sine and cosne curve from -2pi to 2pi")
plot.legend(['sinx','cosx'])
plot.grid(True, which='both')
plot.show()