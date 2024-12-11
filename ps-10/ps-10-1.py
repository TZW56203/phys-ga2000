import numpy as np
import matplotlib.pyplot as plt

def psivec(x):
    x0 = L / 2
    sigma = 1e-10  # m
    kappa = 5e10 # m^{-1}
    
    return np.exp(- np.square(x - x0) / (2 * sigma**2)) * np.exp(1j * kappa * x)

def tridiag(n, main, up, low):
    M = np.zeros((n, n), dtype = complex)
    np.fill_diagonal(M, main)
    np.fill_diagonal(M[:, 1:], up)
    np.fill_diagonal(M[1:, :], low)
    return M

def CNstep(psi):
    v = np.dot(B, psi)
    x = np.linalg.solve(A, v)
    return x


m = 9.109e-31  # kg
hbar = 6.626e-34 / (2 * np.pi)  # J s
L = 1e-8  # m

N = 1000
a = L / N

h = 1e-18  # s

a1 = 1 + h * 1j * hbar / (2 * m * a**2)
a2 = -h * 1j * hbar / (4 * m * a**2)
b1 = 1 - h * 1j * hbar / (2 * m * a**2)
b2 = h * 1j * hbar / (4 * m * a**2)

A = tridiag(N, a1, a2, a2)
B = tridiag(N, b1, b2, b2)

nstep = 2000
psi = np.zeros((nstep, N), dtype = complex)
x = a * np.arange(1, N + 1, 1)
psi[0] = psivec(x)

for i in range(nstep-1):
    psi[i+1] = CNstep(psi[i])
    
np.save('psi-1.npy', psi)

nfig = 4
for i in range(nfig):
    fig, ax = plt.subplots(dpi=200)
    ax.plot(x, np.real(psi[i * nstep // nfig]))
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, L)
    plt.show()
    
