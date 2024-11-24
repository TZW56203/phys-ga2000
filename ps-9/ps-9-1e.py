import numpy as np
import matplotlib.pyplot as plt

def f(r, t, mu):
    omega = 1
    x = r[0]
    y = r[1]
    fx = y
    fy = mu * (1 - x**2) * y - omega**2 * x
    return np.array([fx, fy], float)

a = 0.
b = 20.
N = 5000
h = (b - a) / N

tpts = np.arange(a, b + h, h)

fig, ax = plt.subplots(dpi=200)
for mu in np.array([1., 2. ,4.]):
    xpts = []
    ypts = []
    r = np.array([1, 0.])
    for t in tpts:
        xpts.append(r[0])
        ypts.append(r[1])
        k1 = h * f(r, t, mu)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h, mu)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h, mu)
        k4 = h * f(r + k3, t + h, mu)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        
    ax.plot(xpts, ypts, label = rf'$\mu$ = {mu}')

ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$dx/dt$')
ax.set_title('van der Pol oscillator phase space')

fig.tight_layout()
fig.savefig('ps-9-1e.png')
fig.show()