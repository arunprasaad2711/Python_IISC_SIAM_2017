from scipy.signal import butter, lfilter
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


n = 100
Lstart = 0
Lend = 100
Lt = Lend - Lstart

t = np.linspace(Lstart, Lend, n)
y = 1.0*np.cos(2.0*np.pi*5*t/Lt)  + 1.0*np.sin(2.0*np.pi*10*t/Lt) + 0.5*np.sin(2.0*np.pi*20*t/Lt)
act = 1.0*np.cos(2.0*np.pi*5*t/Lt)  + 1.0*np.sin(2.0*np.pi*10*t/Lt)

'''cut off values'''
dt = t[1] - t[0]
fs = 2.0 # sampling frequency
highcut = 1.0/(7.0*Lt)
lowcut = 1.0/(15.0*Lt)

# Fourier filter
freqs = fftfreq(n)
idx = np.argsort(freqs)

nwaves = freqs*n
print(nwaves)
mask = freqs > 0

fft_vals = fft(y)

fft_new = np.copy(fft_vals)
fft_new[(nwaves==20) & (nwaves==-20)] = 0.0
filt_data = ifft(fft_new)

# butterworth filter
b_filt = butter_bandpass_filter(y, lowcut, highcut, fs, order=3)

plt.figure(1)
plt.plot(t, y, color='red', label='signal')
plt.legend()
plt.show()

plt.figure(2)
#plt.plot(t, y, color='red', label='original signal')
plt.plot(t, act, color='green', label='true filtered signal')
#plt.plot(t, filt_data, color='blue', label='fourier filtered signal')
plt.plot(t, b_filt, color='black', label='butterworth filtered signal')
plt.legend()
plt.show()




