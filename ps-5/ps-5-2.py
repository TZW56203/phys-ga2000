import numpy as np
import matplotlib.pyplot as plt

def f(a, x):
    return np.power(x, a-1) * np.exp(-x)

def f_alt(a, x):
    return np.exp((a-1) * np.log(x) - x)

def gamma(a):
    y = (a - 1) * zp / (1 - zp)
    return np.sum((a - 1) / np.square(1 - zp) * wp * f_alt(a, y))


# (a)
xs = np.arange(0, 5.05, 0.05)

fig, ax = plt.subplots(dpi=200)
ax.plot(xs, f(2, xs), label='a = 2')
ax.plot(xs, f(3, xs), label='a = 3')
ax.plot(xs, f(4, xs), label='a = 4')
ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$x^{a-1}e^{-x}$')
ax.set_title(r'$x^{a-1}e^{-x}$')

fig.tight_layout()
plt.savefig('ps-5-2a.png')
plt.show()


# (e)
N_leg = 100
z, w = np.polynomial.legendre.leggauss(N_leg)

a = 0
b = 1
zp = (b - a) / 2 * z + (b + a) / 2
wp = (b - a) / 2 * w

print('gamma(3/2) =', gamma(3/2))
print('gamma(3) =', gamma(3))
print('gamma(6) =', gamma(6))
print('gamma(10) =', gamma(10))