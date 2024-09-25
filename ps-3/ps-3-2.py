import numpy as np
import matplotlib.pyplot as plt

seed = 12345
rng = np.random.default_rng(seed)

NBi213 = 10000
NPb = 0
NTl = 0
NBi209 = 0

tau_Pb = 3.3 * 60
tau_Tl = 2.2 * 60
tau_Bi = 46 * 60

h = 1.0  # Size of time-step in seconds

p_Pb = 1 - 2**(-h / tau_Pb)
p_Tl = 1 - 2**(-h / tau_Tl)
p_Bi = 1 - 2**(-h / tau_Bi)

tmax = 20000

t_pts = np.arange(0, tmax, h)
Bi213_pts = np.zeros(t_pts.shape)
Pb_pts = np.zeros(t_pts.shape)
Tl_pts = np.zeros(t_pts.shape)
Bi209_pts = np.zeros(t_pts.shape)

for i, t in enumerate(t_pts):
    Bi213_pts[i] = NBi213
    Pb_pts[i] = NPb
    Tl_pts[i] = NTl
    Bi209_pts[i] = NBi209
    
    decay_Pb = 0
    for j in range(NPb):
        if rng.random() < p_Pb:
            decay_Pb += 1
    
    NPb -= decay_Pb
    NBi209 += decay_Pb
    
    decay_Tl = 0
    for j in range(NTl):
        if rng.random() < p_Tl:
            decay_Tl += 1
    
    NTl -= decay_Tl
    NPb += decay_Tl
    
    decay_Bi_Pb = 0
    decay_Bi_Tl = 0
    for j in range(NBi213):
        if rng.random() < p_Bi:
            if rng.random() < 0.9791:
                decay_Bi_Pb += 1
            else:
                decay_Bi_Tl += 1
    
    NBi213 -= (decay_Bi_Pb + decay_Bi_Tl)
    NPb += decay_Bi_Pb
    NTl += decay_Bi_Tl
    
    
# plot
fig, ax = plt.subplots()
ax.plot(t_pts, Bi213_pts, label = 'Bi_213')
ax.plot(t_pts, Pb_pts, label = 'Pb')
ax.plot(t_pts, Tl_pts, label = 'Tl')
ax.plot(t_pts, Bi209_pts, label = 'Bi_209')
ax.legend()
ax.set_xlabel('time (s)')
ax.set_ylabel('N')

ax.set_title('Radioactive decay chain')
plt.savefig('ps-3-2.png')
plt.show()



    
