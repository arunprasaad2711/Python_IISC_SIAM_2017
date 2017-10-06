import numpy as np
from scipy.integrate.quadpack import quad
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use('classic')

b = 5.0

# Function which is to be integrated
def func(x):
    return np.array(x**2) 

x = np.linspace(-10, 10, 201)
integral, err = quad(func, 1, 5)
# Numerical quadrature that calculates the integral and error

print("The integral is :", integral)
print("The error is :", err)

section = np.linspace(-5, 5, 20)

plt.plot(x, func(x), label='Function', color='b')
plt.fill_between(section, func(section), facecolor='red')
plt.grid()
plt.legend()
plt.title('Area under the curve')
plt.show()
