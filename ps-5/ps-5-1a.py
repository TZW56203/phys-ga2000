import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1 + 1/2 * np.tanh(2 * x)

def f_p_ana(x):
    return 1 / np.square(np.cosh(2 * x))

def f_p_num(x, h=0.01):
    return (f(x + h/2) - f(x - h/2)) / h


xs = np.arange(-2, 2.05, 0.05)

# plot
fig, ax = plt.subplots(dpi=200)
ax.plot(xs, f_p_ana(xs), label='analytical')
ax.scatter(xs, f_p_num(xs), label='numerical', s=15, c ='orange')
ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_title(r'Central difference $h$ = 0.01')

fig.tight_layout()
plt.savefig('ps-5-1a.png')
plt.show()