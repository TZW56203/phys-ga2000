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


# (a)
psi_0 = make_psi(0)
psi_1 = make_psi(1)
psi_2 = make_psi(2)
psi_3 = make_psi(3)

x_a = np.linspace(-4, 4, 101)

fig, ax = plt.subplots(dpi=200)
ax.plot(x_a, psi_0(x_a), label='n = 0')
ax.plot(x_a, psi_1(x_a), label='n = 1')
ax.plot(x_a, psi_2(x_a), label='n = 2')
ax.plot(x_a, psi_3(x_a), label='n = 3')
ax.legend()

ax.set_xlabel('x')
ax.set_ylabel(r'$\psi_n$(x)')
ax.set_title('QHO wave functions for n = 0, 1, 2, 3')

fig.tight_layout()
plt.savefig('ps-4-3a.png')
plt.show()


# (b)
psi_30 = make_psi(30)

x_b = np.linspace(-10, 10, 201)

fig, ax = plt.subplots(dpi=200)
ax.plot(x_b, psi_30(x_b))

ax.set_xlabel('x')
ax.set_ylabel(r'$\psi_n$(x)')
ax.set_title('QHO wave function for n = 30')

fig.tight_layout()
plt.savefig('ps-4-3b.png')
plt.show()





