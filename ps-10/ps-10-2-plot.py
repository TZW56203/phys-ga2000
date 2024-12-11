import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

m = 9.109e-31  # kg
hbar = 6.626e-34 / (2 * np.pi)  # J s
L = 1e-8  # m

N = 1000
a = L / N

x = a * np.arange(1, N + 1, 1)

ntpt = 2000

psi = np.load('psi-2.npy')

nfig = 4
for i in range(nfig):
    fig, ax = plt.subplots(dpi=200)
    ax.plot(x, psi[i * ntpt // nfig])
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, L)
    ax.set_xlabel(r'$x$ (m)')
    ax.set_ylabel(r'$\psi$')
    fig.tight_layout()
    plt.savefig(f'ps-10-2-{i}.png')
    plt.show()


psi_test = np.load('psi_test.npy')

fig, ax = plt.subplots(dpi=200)
ax.plot(x, psi_test)
ax.set_ylim(-1, 1)
ax.set_xlim(0, L)
ax.set_xlabel(r'$x$ (m)')
ax.set_ylabel(r'$\psi$')
ax.set_title(r'wave function at $t = 10^{-16}$ s')
fig.tight_layout()
plt.savefig('ps-10-2-test.png')
plt.show()

if True:
    fig, ax = plt.subplots(dpi=200)
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, L)
    line, = ax.plot([], [])
    
    def init():
        line.set_data([], [])
        return (line,)
    
    def update(frame):
        line.set_data(x, np.real(psi[frame]))
        return (line,)
    
    anim = animation.FuncAnimation(fig, update, init_func=init, frames=ntpt, interval=1, blit=True)
    anim.save('ps-10-2.gif')
    
print('done')