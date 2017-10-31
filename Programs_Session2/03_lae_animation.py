'''
This is a program for 1D linear advection equation

Ut + c*Ux = 0

Scheme used : Forward Time, Backward Space

Works for small time steps and small grid size
'''

import numpy as np
import matplotlib.pyplot as plt

nx = 100    # Number of grid points
nt = 101    # Number of time points
L = 10      # Length of Domain
A = 1.0     # Amplitude of wave
c = 1.0     # wave velocity
T = 10.0    # Total Seconds for time march

# Grid points
x1 = np.linspace(0, L, nx+1)
x = x1[:-1]

# Time steps
t = np.linspace(0, T, nt)

dx = x[1] - x[0]    # grid size
dt = t[1] - t[0]    # time step in seconds

# Computational Parameters
R = c*dt/dx     # CFL number
F = 1.0 - R     # multiplying factor

# Initial condition for U
uinit = A*np.sin(2.0*np.pi*x/L)

uold = np.copy(uinit)
unew = np.zeros(nx)

def march(Unew, Uold, f1, f2):

    # Calculation along the grid
    unew[1:] = f1 * Uold[1:] + f2 * Uold[0:-1]
    # Boundary Condition
    unew[0] = uold[-1]

    # Swapping the values for future use
    Uold[:] = Unew

    return Uold, Unew

# To enable interactive plotting
plt.ion()
plt.figure()
plt.plot(x, uinit, color='xkcd:black', label='Initial Velocity profile')
plt.plot(x, uold , color='xkcd:salmon', label='Current Velocity profile')  # Contour plotting the values
plt.xlabel('Length', fontsize=10)  # X axis label
plt.ylabel('Velocity in $m/s$', fontsize=10)  # Y axis label
plt.title('Wave advection in a 1D domain')
string = 'Time $t$ = '+str(t[0])+' s, $U_{max}$ = '+str(np.amax(uold))+' $m/s$, $U_{min}$ = '+str(np.amin(uold))+'$m/s$'
plt.suptitle(string)
plt.legend()
plt.grid(True)  # Enabling gridding
plt.axis((-0.1, 10.1, -1.2, 1.2))  # Making axis rigid
plt.pause(0.01)

for i in range(0, nt):

    # Calculation along the grid
    # unew[1:] = F*uold[1:] + R*uold[0:-1]
    # Boundary Condition
    # unew[0] = uold[-1]

    # Swapping the values for future use
    # uold[:] = unew

    uold, unew = march(Unew=unew, Uold=uold, f1=F, f2=R)

    plt.clf()
    plt.plot(x, uinit, color='xkcd:black', label='Initial Velocity profile')
    plt.plot(x, uold , color='xkcd:salmon', label='Current Velocity profile')  # Contour plotting the values
    plt.xlabel('Length', fontsize=10)  # X axis label
    plt.ylabel('Velocity in $m/s$', fontsize=10)  # Y axis label
    plt.title('Wave advection in a 1D domain')
    string = 'Time $t$ = ' + str(t[i]) + ' s, $U_{max}$ = ' + str(np.amax(uold)) + ' $m/s$, $U_{min}$ = ' + str(
        np.amin(uold)) + '$m/s$'
    plt.suptitle(string)
    plt.legend()
    plt.grid(True)  # Enabling gridding
    plt.axis((-0.1, 10.1, -1.2, 1.2))  # Making axis rigid
    plt.pause(0.01)

