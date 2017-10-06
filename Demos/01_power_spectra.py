# Program to try and work out the power spectrum

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft

n = 256
Lx = 100

x = np.linspace(0, Lx, n)
y = 1.0*np.cos(2.0*np.pi*5*x/Lx)  + 1.0*np.sin(2.0*np.pi*10*x/Lx) + 0.5*np.sin(2.0*np.pi*20*x/Lx)
act = 1.0*np.cos(2.0*np.pi*5*x/Lx)  + 1.0*np.sin(2.0*np.pi*10*x/Lx)

mean_y = np.mean(y)
std_y = np.std(y)
var_y = std_y**2.0

print(mean_y, std_y, var_y)

freqs = fftfreq(n)
idx = np.argsort(freqs)

nwaves = freqs*n
mask = freqs > 0

fft_vals = fft(y)

fft_new = np.copy(fft_vals)
fft_new[nwaves==20] = 0.0
fft_new[nwaves==-20] = 0.0
filt_data = ifft(fft_new)

# amplitudes
amp = 2.0*np.abs(fft_vals/n)

# this is the power spectra
ps = 2.0*np.abs(fft_vals/n)**2.0

# power by variance
pow_var = ps/var_y*100.0

# freq.power spectra
fps = ps*freqs

#print(fft_vals)
#print(np.abs(fft_vals*2.0/n))
print(np.sum(ps[mask]))

plt.figure(1)
plt.plot(nwaves[mask], ps[mask])
#plt.plot(x, y, color='xkcd:salmon', label='original')
#plt.plot(x, filt_data, color='black', label='filtered')
#plt.plot(x, act, color='cyan', label='actual')
plt.legend()

plt.figure(2)
#plt.plot(nwaves[mask], pow_var[mask])
plt.plot(x, y, color='xkcd:salmon', label='original')
plt.plot(x, filt_data, color='black', label='filtered')
plt.plot(x, act, color='cyan', label='actual')
plt.legend()
plt.show()
