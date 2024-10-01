import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (np.power(x, 4) * np.exp(x) / np.square(np.exp(x) - 1))

def cv(T, N):
    V = 1000 * 1e-6  # unit: m
    theta_D = 428
    rho = 6.022e28
    
    x, w = np.polynomial.legendre.leggauss(N)
    
    a = 0
    b = theta_D / T
    
    xp = (b - a) / 2 * x + (b + a) / 2
    wp = (b - a) / 2 * w
    
    intf = np.sum(wp * f(xp))
    
    Cv = 9 * V * rho * k * np.power(T/theta_D, 3) * intf
    
    return Cv


k = 1.38e-23

T1 = 298
T2 = 5

Ns = np.arange(10, 80, 10)
Cvs1 = np.zeros(Ns.shape)
Cvs2 = np.zeros(Ns.shape)

for i, N in enumerate(Ns):
    Cvs1[i] = cv(T1, N)
    Cvs2[i] = cv(T2, N)

# plot
fig, ax = plt.subplots(dpi=200)
ax.plot(Ns, Cvs1)
ax.set_xlabel('N')
ax.set_ylabel(r'$C_v$ (J/K)')
ax.set_title(fr'$C_v$ vs N with T = {T1} K')

fig.tight_layout()
plt.savefig(f'ps-4-1c_T{T1}.png')
plt.show()


fig, ax = plt.subplots(dpi=200)
ax.plot(Ns, Cvs2)
ax.set_xlabel('N')
ax.set_ylabel(r'$C_v$ (J/K)')
ax.set_title(rf'$C_v$ vs N with T = {T2} K')

fig.tight_layout()
plt.savefig(f'ps-4-1c_T{T2}.png')
plt.show()