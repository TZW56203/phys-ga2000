import numpy as np
import matplotlib.pyplot as plt

def f(r, t):
    omega = 1
    x = r[0]
    y = r[1]
    fx = y
    fy = - omega**2 * x
    return np.array([fx, fy], float)

def f_an(r, t):
    omega = 1
    x = r[0]
    y = r[1]
    fx = y
    fy = - omega**2 * x**3
    return np.array([fx, fy], float)

a = 0.
b = 50.
N = 5000
h = (b - a) / N

tpts = np.arange(a, b + h, h)

# harmonic
fig, ax = plt.subplots(dpi=200)
for i in np.array([1., 2. ,3.]):
    xpts = []
    ypts = []
    r = np.array([i, 0.])
    for t in tpts:
        xpts.append(r[0])
        ypts.append(r[1])
        k1 = h * f(r, t)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(r + k3, t + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        
    ax.plot(tpts, xpts, label = f'x(0)={i}')

ax.legend()
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$x$')
ax.set_title('harmonic oscillator')

fig.tight_layout()
fig.savefig('ps-9-1ab.png')
fig.show()

# anharmonic
fig, ax = plt.subplots(dpi=200)
fig2, ax2 = plt.subplots(dpi=200)
for i in np.array([1., 1.05 ,1.1]):
    xpts = []
    ypts = []
    r = np.array([i, 0.])
    for t in tpts:
        xpts.append(r[0])
        ypts.append(r[1])
        k1 = h * f_an(r, t)
        k2 = h * f_an(r + 0.5 * k1, t + 0.5 * h)
        k3 = h * f_an(r + 0.5 * k2, t + 0.5 * h)
        k4 = h * f_an(r + k3, t + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        
    ax.plot(tpts, xpts, label = f'x(0)={i}')
    ax2.plot(xpts, ypts, label = f'x(0)={i}')

ax.legend()
ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$x$')
ax.set_title('anharmonic oscillator')

fig.tight_layout()
fig.savefig('ps-9-1c.png')
fig.show()

ax2.legend()
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$dx/dt$')
ax2.set_title('anharmonic oscillator phase space')

fig2.tight_layout()
fig2.savefig('ps-9-1d.png')
fig2.show()


