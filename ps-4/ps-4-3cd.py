import numpy as np
import matplotlib.pyplot as plt
import math

def H(n, x):
    if n == 0:
        return 1
    
    elif n == 1:
        return 2 * x
    
    else:
        return 2 * x * H(n-1, x) - 2 * (n-1) * H(n-2, x)


def make_psi(n):
    def psi(x):
        return 1 / np.sqrt(np.exp2(n) * math.factorial(n) * np.sqrt(np.pi)) * np.exp(-np.square(x)/2) * H(n, x)
    return psi


def make_poly(n):
    def poly(x):
        return 1 / np.sqrt(np.exp2(n) * math.factorial(n) * np.sqrt(np.pi)) * H(n, x)
    return poly


# (c)
psi_5 = make_psi(5)

N_leg = 100

z, w = np.polynomial.legendre.leggauss(N_leg)
zsq = np.square(z)

y = (1 + zsq) / np.square(1 - zsq) * np.square(z / (1 - zsq) * psi_5(z / (1 - zsq)))

var = np.sum(w * y)
rms = np.sqrt(var)

print('Analytical:', np.sqrt(11/2))
print(f'Gauss-Legendre quadrature (N={N_leg}):', rms)
print(f'Gauss-Legendre difference (N={N_leg}):', rms - np.sqrt(11/2))


# (d)
poly_5 = make_poly(5)

N_herm = 7  # vary this

x, w = np.polynomial.hermite.hermgauss(N_herm)

y = np.square(x * poly_5(x))

var = np.sum(w * y)
rms = np.sqrt(var)

print(f'Gauss-Hermite quadrature (N={N_herm}):', rms)
print(f'Gauss-Hermite difference (N={N_herm}):', rms - np.sqrt(11/2))


