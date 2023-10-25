import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,10])
y=np.array([-1,-30])

plt.plot(x,y)
#to plot only points:-> plt.plot(x,y,'o')
#linestyle='dotted' or solid, dashed, dashdot
plt.show()