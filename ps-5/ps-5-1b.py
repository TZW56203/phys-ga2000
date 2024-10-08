import numpy as np
import jax
import jax.numpy as jnp
import matplotlib.pyplot as plt

def f(x):
    return 1 + 1/2 * jnp.tanh(2 * x)

def f_p_ana(x):
    return 1 / jnp.square(jnp.cosh(2 * x))

def f_p_num(x, h=0.01):
    return (f(x + h/2) - f(x - h/2)) / h

f_p_jax = jax.grad(f)

xs = jnp.arange(-2, 2.05, 0.05)

# plot
fig, ax = plt.subplots(dpi=200)
ax.plot(xs, f_p_ana(xs), label='analytical')
ax.scatter(xs, jax.vmap(f_p_jax)(xs), label='jax', s=15, c ='orange')
ax.legend()
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_title('jax')

fig.tight_layout()
plt.savefig('ps-5-1b.png')
plt.show()

print('analytical:', "f'(0) =", f_p_ana(0))
print('central difference (h=0.01):', "f'(0) =", f_p_num(0))
print('jax:', "f'(0) =", f_p_jax(0.), end='\n\n')

print('analytical:', "f'(2) =", f_p_ana(2))
print('central difference (h=0.01):', "f'(2) =", f_p_num(2))
print('jax:', "f'(2) =", f_p_jax(2.))