from scipy.constants import codata
import numpy as np
from scipy.integrate.quadpack import quad
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use('classic')

# get physical from module:
D = codata.physical_constants

s = D['Stefan-Boltzmann constant'][0]

def spectra(l,T):
    h = D['Planck constant'][0]
    k = D['Boltzmann constant'][0]
    c = D['speed of light in vacuum'][0]
    func = ((2.0*h*np.pi*c**2)/(l**5))/(np.exp(h*c/(l*k*T)) - 1.0)
    return func

T1 = 5770.0
T2 = 6000.0
T3 = 5000.0
T4 = 4000.0

int1,err1 = quad(spectra, 0.38e-6, 0.78e-6, args=(T1))

E1 = s*T1**4

l = np.linspace(0, 5e-6, 201)

s1 = spectra(l, T1)
s2 = spectra(l, T2)
s3 = spectra(l, T3)
s4 = spectra(l, T4)

print("The total Energy flux is :", E1)
print("The Energy flux in the band is :", int1)
print("The Energy flux Fraction is:", int1/E1)
print("The error is :", err1)

section = np.linspace(0.38e-6, 0.78e-6, 20)

plt.plot(l*1e6, s1, 'k', label='T = 5770 K')
plt.plot(l*1e6, s2, 'b', label='T = 6000 K')
plt.plot(l*1e6, s3, 'g', label='T = 5000 K')
plt.plot(l*1e6, s4, 'y', label='T = 4000 K')
plt.fill_between(section*1e6, spectra(section, T1), facecolor='red')
plt.legend()
plt.grid('on')
plt.axis([0.0, 5.0, 0.0e13, 10.5e13])
plt.xticks(np.linspace(0.0, 5.0, 11))
plt.yticks(np.linspace(0.0e13, 10.5e13, 20))
plt.xlabel('Wavelength in $\mu m$')
plt.ylabel('Irradiance in $Wm^{-2}\mu m^{-1}$')
plt.suptitle('Session 3 Demo')
plt.title("Integral of Planck's Spectral Emission Curves")
plt.savefig('Spectra.png', format='png', dpi=400)
plt.show()
