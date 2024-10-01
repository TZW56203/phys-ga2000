import numpy as np
import matplotlib.pyplot as plt
# from gaussxw import gaussxwab
# from scipy.integrate import fixed_quad, quad


def f(x):
    return (np.power(x, 4) * np.exp(x) / np.square(np.exp(x) - 1))

def cv(T):
    V = 1000 * 1e-6  # unit: m
    theta_D = 428
    rho = 6.022e28
    
    a = 0
    b = theta_D / T
    
    xp = (b - a) / 2 * x + (b + a) / 2
    wp = (b - a) / 2 * w
    
    # xp2, wp2 = gaussxwab(N, a, b)
    
    intf = np.sum(wp * f(xp))
    # intf2 = np.sum(wp2 * f(xp2))
    # intf3, _  = fixed_quad(f, a, b, n=N)
    # intf4, _ = quad(f, a, b)
    
    Cv = 9 * V * rho * k * np.power(T/theta_D, 3) * intf
    # Cv2 = 9 * V * rho * k * np.power(T/theta_D, 3) * intf2
    # Cv3 = 9 * V * rho * k * np.power(T/theta_D, 3) * intf3
    # Cv4 = 9 * V * rho * k * np.power(T/theta_D, 3) * intf4
    
    # print(Cv, Cv2, Cv3, Cv4, sep='\n')
    
    return Cv
    

N = 50
k = 1.38e-23

x, w = np.polynomial.legendre.leggauss(N)  # this takes time and can be reused, so do not repeat it

Ts = np.arange(5, 500, 5)
Cvs = np.zeros(Ts.shape)

for i, T in enumerate(Ts):
    Cvs[i] = cv(T)

# plot
fig, ax = plt.subplots(dpi=200)
ax.plot(Ts, Cvs)
ax.set_xlabel('T (K)')
ax.set_ylabel(r'$C_v$ (J/K)')
ax.set_title(r'$C_v$ vs T')

fig.tight_layout()
plt.savefig('ps-4-1ab.png')
plt.show()

print('cv(298) =', cv(298))
print('cv(500) =', cv(500))
