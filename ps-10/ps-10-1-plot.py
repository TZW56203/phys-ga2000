import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

m = 9.109e-31  # kg
hbar = 6.626e-34 / (2 * np.pi)  # J s
L = 1e-8  # m

N = 1000
a = L / N

h = 1e-18  # s

nstep = 2000

x = a * np.arange(1, N + 1, 1)

psi = np.load('psi-1.npy')

nfig = 4
for i in range(nfig):
    fig, ax = plt.subplots(dpi=200)
    ax.plot(x, np.real(psi[i * nstep // nfig]))
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, L)
    ax.set_xlabel(r'$x$ (m)')
    ax.set_ylabel(r'$\psi$')
    fig.tight_layout()
    plt.savefig(f'ps-10-1-{i}.png')
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
    
    anim = animation.FuncAnimation(fig, update, init_func=init, frames=nstep, interval=1, blit=True)
    anim.save('ps-10-1.gif')
    
print('done')