import numpy as np
import matplotlib.pyplot as plt

def f(r, t, k):
    xp = r[0]
    vx = r[1]
    yp = r[2]
    vy = r[3]
    
    fxp = vx
    fvx = - np.pi / 2 * k * vx * np.sqrt(vx**2 + vy**2)
    fyp = vy
    fvy = -1 - np.pi / 2 * k * vy * np.sqrt(vx**2 + vy**2)

    return np.array([fxp, fvx, fyp, fvy])

a = 0.
b = 1.
N = 5000
h = (b - a) / N

tppts = np.arange(a, b + h, h)

fig, ax = plt.subplots(dpi=200)
fig2, ax2 = plt.subplots(dpi=200)

for m in np.array([1, 2, 3]):
    R = 0.08
    rho = 1.22
    C = 0.47
    g = 9.8
    coeff = R**2 * rho * C * g / m
    T = 50
    k = coeff * T**2
    
    xppts = []
    vxpts = []
    yppts = []
    vypts = []
    
    r = np.array([0., 50 * np.sqrt(3) / (g * T), 0., 50 / (g * T)])
    for t in tppts:
        xppts.append(r[0])
        vxpts.append(r[1])
        yppts.append(r[2])
        vypts.append(r[3])
        k1 = h * f(r, t, k)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h, k)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h, k)
        k4 = h * f(r + k3, t + h, k)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        
        if r[2] < 0:
            break
    
    xppts = np.array(xppts)
    yppts = np.array(yppts)
    ax.plot(xppts, yppts, label = rf'$m$ = {m} kg')
    ax2.plot(xppts * (g * T**2), yppts * (g * T**2), label = rf'$m$ = {m} kg')

ax.legend()
ax.set_xlabel(r'$x^\prime = \frac{x}{gT^2}$')
ax.set_ylabel(r'$y^\prime = \frac{y}{gT^2}$')
ax.set_title(r'Trajectory $y^\prime-x^\prime$')

fig.tight_layout()
fig.savefig('ps-9-2.png')
fig.show()

ax2.legend()
ax2.set_xlabel(r'$x$ (m)')
ax2.set_ylabel(r'$y$ (m)')
ax2.set_title(r'Trajectory $y-x$')

fig2.tight_layout()
fig2.savefig('ps-9-2unit.png')
fig2.show()


fig, ax = plt.subplots(dpi=200)

for k in np.array([1, 2, 3]):
    g = 9.8
    T = 50
    
    xppts = []
    vxpts = []
    yppts = []
    vypts = []
    
    r = np.array([0., 50 * np.sqrt(3) / (g * T), 0., 50 / (g * T)])
    for t in tppts:
        xppts.append(r[0])
        vxpts.append(r[1])
        yppts.append(r[2])
        vypts.append(r[3])
        k1 = h * f(r, t, k)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h, k)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h, k)
        k4 = h * f(r + k3, t + h, k)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        
        if r[2] < 0:
            break
    
    ax.plot(xppts, yppts, label = rf'$k$ = {k}')

ax.legend()
ax.set_xlabel(r'$x^\prime = \frac{x}{gT^2}$')
ax.set_ylabel(r'$y^\prime = \frac{y}{gT^2}$')
ax.set_title('Trajectory')

fig.tight_layout()
fig.savefig('ps-9-2alt.png')
fig.show()


