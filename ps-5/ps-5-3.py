import numpy as np
import matplotlib.pyplot as plt


with open('my_signal.dat', 'w') as mysig:
    with open('signal.dat', 'r') as sig:
        for line in sig:
            mysig.write(line.replace('|', ' '))


t, b = np.loadtxt('my_signal.dat', unpack=True, skiprows=1)


# (a)
fig, ax = plt.subplots(dpi=200)
ax.scatter(t, b, s=10)
ax.set_xlabel('time')
ax.set_ylabel('signal')
ax.set_title('Signal')

fig.tight_layout()
plt.savefig('ps-5-3a.png')
plt.show()


# (b) (c)
tp = (t - np.mean(t)) / np.std(t)

order_b = 3

B = np.ones((len(tp), order_b + 1))
for i in range(1, order_b + 1):
    B[:, i] = np.power(tp, i)

(u, w, vt) = np.linalg.svd(B, full_matrices=False)

print('condition number (3rd order):', np.max(w) / np.min(w))

Binv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = Binv.dot(b)
bm = B.dot(x)

print('r =',np.sqrt(np.sum(np.square(bm - b))))
print('r / sqrt(N) =', np.sqrt(np.sum(np.square(bm - b)) / len(tp)), '\n')

# print(Binv)
# print(np.linalg.pinv(B))

fig, ax = plt.subplots(dpi=200)
ax.plot(t, b, '.', label='data')
ax.plot(t, bm, '.', label='model')
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('signal')
ax.set_title('SVD 3rd order polynomial fit')

fig.tight_layout()
plt.savefig('ps-5-3b.png')
plt.show()


# (d)
order_d = 23

D = np.ones((len(tp), order_d + 1))
for i in range(1, order_d + 1):
    D[:, i] = np.power(tp, i)

(u, w, vt) = np.linalg.svd(D, full_matrices=False)

print(f'condition number ({order_d}th order):', np.max(w) / np.min(w))

Dinv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = Dinv.dot(b)
bm = D.dot(x)

print('r =',np.sqrt(np.sum(np.square(bm - b))))
print('r / sqrt(N) =', np.sqrt(np.sum(np.square(bm - b)) / len(tp)), '\n')

fig, ax = plt.subplots(dpi=200)
ax.plot(t, b, '.', label='data')
ax.plot(t, bm, '.', label='model')
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('signal')
ax.set_title(f'SVD {order_d}th order polynomial fit')

fig.tight_layout()
plt.savefig('ps-5-3d.png')
plt.show()


# (e)
l = (np.max(tp) - np.min(tp)) / 2
# l = (1.1e8 - np.mean(t)) / np.std(t) / 2

term = 21

E = np.ones((len(tp), term))
for i in range(1, term):
    if i % 2 == 1:
        E[:, i] = np.sin(((i + 1)/2 + 1) * np.pi * tp / l)
    else:
        E[:, i] = np.cos((i/2 + 1) * np.pi * tp / l)

# for i in range(1, order_e + 1, 2):
#     E[:, i] = np.cos(2 * np.pi * tp / l * (i+1)/2)
#     E[:, i+1] = np.sin(2 * np.pi * tp / l * (i+1)/2)

(u, w, vt) = np.linalg.svd(E, full_matrices=False)

print(f'condition number ({term} term):', np.max(w) / np.min(w))

Einv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = Einv.dot(b)
bm = E.dot(x)

print('r =',np.sqrt(np.sum(np.square(bm - b))))
print('r / sqrt(N) =', np.sqrt(np.sum(np.square(bm - b)) / len(tp)), '\n')

fig, ax = plt.subplots(dpi=200)
ax.plot(t, b, '.', label='data')
ax.plot(t, bm, '.', label='model')
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('signal')
ax.set_title(f'SVD {term} term Fourier series fit')

fig.tight_layout()
plt.savefig('ps-5-3e.png')
plt.show()


term = 300

E = np.ones((len(tp), term))
for i in range(1, term):
    if i % 2 == 1:
        E[:, i] = np.sin(((i + 1)/2 + 1) * np.pi * tp / l)
    else:
        E[:, i] = np.cos((i/2 + 1) * np.pi * tp / l)

# for i in range(1, order_e + 1, 2):
#     E[:, i] = np.cos(2 * np.pi * tp / l * (i+1)/2)
#     E[:, i+1] = np.sin(2 * np.pi * tp / l * (i+1)/2)

(u, w, vt) = np.linalg.svd(E, full_matrices=False)

print(f'condition number ({term} term):', np.max(w) / np.min(w))

Einv = vt.transpose().dot(np.diag(1. / w)).dot(u.transpose())
x = Einv.dot(b)
bm = E.dot(x)

print('r =',np.sqrt(np.sum(np.square(bm - b))))
print('r / sqrt(N) =', np.sqrt(np.sum(np.square(bm - b)) / len(tp)))

fig, ax = plt.subplots(dpi=200)
ax.plot(t, b, '.', label='data')
ax.plot(t, bm, '.', label='model')
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('signal')
ax.set_title(f'SVD {term} term Fourier series fit')

fig.tight_layout()
plt.savefig('ps-5-3e2.png')
plt.show()


