import numpy as np
import matplotlib.pyplot as plt


def gaussian (x, mu, sig):
    return (
        1 / (sig * np.sqrt(2 * np.pi)) * np.exp(- 1/2 * np.power((x-mu)/sig, 2))
    )

x = np.arange(-10, 10.1, 0.1)
mu = 0
sig = 3

fig, ax = plt.subplots()
ax.plot(x, gaussian(x, mu, sig))
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'A Gaussian with mean {mu} and standard deviation {sig}')
plt.savefig('gaussian.png')
plt.show()

