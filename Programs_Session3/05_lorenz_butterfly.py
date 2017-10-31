import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from NumIntLib import rk_schemes as rk

def lorenz(st, t, s, p, b):
    
    x0 = st[0] # x displacement
    y0 = st[1] # y displacement
    z0 = st[2] # z displacement
    
    xd = s*(y0-x0)
    yd = (p-z0)*x0 - y0
    zd = x0*y0 - b*z0
    
    return xd, yd, zd

s = 10.0
p = 28.0
b = 8.0/3.0

init = [1.0, 1.0, 1.0]
params = (s, p, b)
t = np.arange(0.0, 60.0, 0.01)

# st = odeint(lorentz, init, t, args=params)
st = rk.rk4(lorenz, init, t, args=params)

x = st[:,0]
y = st[:,1]
z = st[:,2]

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x, y, z, 'r', label='Lorenz Butterfly')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.savefig('Lorenz_Butterfly.png', format='png', dpi=400)
