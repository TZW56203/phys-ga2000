import numpy as np
# import jax
# import jax.numpy as jnp

# mass in kg
m_e = 5.972e24
m_m = 7.346e22
m_s = 1.989e30
m_j = 1.898e27

# radius in m
r_e = 149598023e3
r_m = 385000e3


def f(rp):
    return 1 - np.power(rp, 3) - mp * np.square(rp / (1 - rp))

def fp(rp):
    return - 3 * np.square(rp) - mp * 2 * rp / np.power(1 - rp, 3)

# fp_jax = jax.grad(f)

def newton(xst=.5):
    tol = 1e-7
    maxiter = 100
    x = xst
    delta = 1.0
    i = 0
    while i < maxiter and np.abs(delta) > tol:
        delta = f(x) / fp(x)
        x -= delta
        i = i + 1
    print('iteration:', i)
    return x

# Moon Earth
print('Moon Earth')
mp = m_m / m_e
L1 = newton()
print('dist to the smaller mass:', r_m * (1- L1) / 1e3, 'km')
print('dist to the larger mass:', r_m * L1 / 1e3, 'km', '\n')

# Earth Sun
print('Earth Sun')
mp = m_e / m_s
L1 = newton()
print('dist to the smaller mass:', r_e * (1 - L1) / 1e3, 'km')
print('dist to the larger mass:', r_e * L1 / 1e3, 'km', '\n')

# Jupiter at Earth dist Sun
print('Jupiter at Earth dist Sun')
mp = m_j / m_s
L1 = newton()
print('dist to the smaller mass:', r_e * (1 - L1) / 1e3, 'km')
print('dist to the larger mass:', r_e * L1 / 1e3, 'km', '\n')