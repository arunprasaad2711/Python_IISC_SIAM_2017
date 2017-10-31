import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use('classic')

x = np.linspace(0, 2.0*np.pi, 100)
y = np.sin(2*x)
y1 = np.gradient(y, x[1]-x[0]) # Calculates the Differential
y2 = np.gradient(y1, x[1]-x[0])

plt.plot(x, y, label='sin(2*x)')
plt.plot(x, y1, label='2cos(2x)')
plt.plot(x, y2, label='-4sin(2x)')
plt.legend()
plt.grid()
plt.savefig('Differentiation.png', format='png', dpi=400)
plt.show()
