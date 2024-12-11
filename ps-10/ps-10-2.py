import numpy as np
import matplotlib.pyplot as plt
import scipy.fft

def psivec(x):
    x0 = L / 2
    sigma = 1e-10  # m
    kappa = 5e10 # m^{-1}
    
    return np.exp(- np.square(x - x0) / (2 * sigma**2)) * np.exp(1j * kappa * x)

def psi2(t):
    k = np.arange(N)
    coeff = np.pi**2 * hbar * k**2 / (2 * m * L**2)
    p1 = alpha * np.cos(coeff * t)
    p2 = eta * np.sin(coeff * t)  # different to Newmann from a sign
    
    psi = scipy.fft.idst(p1 + p2)
    
    return psi
    

m = 9.109e-31  # kg
hbar = 6.626e-34 / (2 * np.pi)  # J s
L = 1e-8  # m

N = 1000
a = L / N

x = a * np.arange(1, N + 1, 1)
psi0 = psivec(x)

psir = np.real(psi0)
psii = np.imag(psi0)

alpha = scipy.fft.dst(psir)
eta = scipy.fft.dst(psii)

h = 1e-18  # s
ntpt = 2000
psi = np.zeros((ntpt, N))
psi[0] = psi0

for i in range(ntpt-1):
    psi[i+1] = psi2((i+1) * h)

np.save('psi-2.npy', psi)

psi_test = psi2(1e-16)
np.save('psi_test.npy', psi_test)

plt.plot(x, psi_test)

nfig = 4
for i in range(nfig):
    fig, ax = plt.subplots(dpi=200)
    ax.plot(x, psi[i * ntpt // nfig])
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, L)
    plt.show()