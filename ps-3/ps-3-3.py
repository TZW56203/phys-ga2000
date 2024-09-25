import numpy as np
import matplotlib.pyplot as plt

seed = 12345
rng = np.random.default_rng(seed)

NTl = 1000

tau = 3.053 * 60
mu  = np.log(2) / tau

z = rng.random(NTl)

t = -1 / mu * np.log(1 - z)
t.sort()

Pb_pts = np.arange(1, 1001, 1)
Tl_pts = 1000 - Pb_pts

# plot
fig, ax = plt.subplots()
ax.plot(t, Tl_pts, label = 'Tl')
ax.plot(t, Pb_pts, label = 'Pb')
ax.legend()
ax.set_xlabel('time (s)')
ax.set_ylabel('N')

ax.set_title('Radioactive decay again')
plt.savefig('ps-3-3.png')
plt.show()

