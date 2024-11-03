import numpy as np
import matplotlib.pyplot as plt

dow = np.loadtxt('dow.txt')

c = np.fft.rfft(dow)
c10 = np.copy(c)
c02 = np.copy(c)

c10[int(dow.size * 0.1):] = 0
c02[int(dow.size * 0.02):] = 0

dow10 = np.fft.irfft(c10)
dow02 = np.fft.irfft(c02)

fig, ax = plt.subplots(dpi=200)
ax.plot(dow, label='dow')
ax.plot(dow10, label='dow10')
ax.plot(dow02, label='dow02')
ax.legend()
ax.set_xlabel('business day')
ax.set_ylabel('Dow Jones Industrial Average')
ax.set_title('Fourier filtering and smoothing')

fig.tight_layout()
plt.savefig('ps-8-3.png')
plt.show()