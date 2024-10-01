import numpy as np
import matplotlib.pyplot as plt

def f(x, a):
    return 1 / np.sqrt(np.power(a, 4) - np.power(x, 4))

def T(a):
    low = 0
    up = a
    
    xp = (up - low) / 2 * x + (up + low) / 2
    wp = (up - low) / 2 * w
    
    intf = np.sum(wp * f(xp, a))
    
    ans = np.sqrt(8 * m) * intf
    
    return ans


m = 1

N = 20

x, w = np.polynomial.legendre.leggauss(N)

a_s = np.arange(0.02, 2.02, 0.02)
T_s = np.zeros(a_s.shape)

for i, a in enumerate(a_s):
    T_s[i] = T(a)
    
# plot
fig, ax = plt.subplots(dpi=200)
ax.plot(a_s, T_s)
ax.set_xlabel('a')
ax.set_ylabel('T')
ax.set_title('T vs a')

fig.tight_layout()
plt.savefig('ps-4-2b.png')
plt.show()


coeff = np.round(np.polyfit(np.log(a_s), np.log(T_s), 1), 3)
eqn = f'y = {coeff[0]}x + {coeff[1]}'

fig, ax = plt.subplots(dpi=200)
ax.plot(np.log(a_s), np.log(T_s), label=eqn)
ax.legend()
ax.set_xlabel('ln(a)')
ax.set_ylabel('ln(T)')
ax.set_title('ln(T) vs ln(a)')

fig.tight_layout()
plt.savefig('ps-4-2c.png')
plt.show()