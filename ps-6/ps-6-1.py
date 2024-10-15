import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import timeit


def eigen1(A):
    ev, evec = np.linalg.eig(A)
    inx = np.argsort(ev)[::-1]
    return ev[inx], evec[:, inx]

def eigen2(A):
    u, w, vt = np.linalg.svd(A)
    ev = np.square(w)
    evec = vt.T
    return ev, evec


# (a)
hdu_list = fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data

wave = np.power(10, logwave)

print('logwave.shape =', logwave.shape)
print('flux.shape =', flux.shape)

nwave = logwave.shape[0]
ngal = flux.shape[0]

print('nwave =', nwave)
print('ngal =', ngal)

# print(np.arange(1, 10))
# print(np.arange(1, 10).shape)
# print(np.zeros(shape = (3,4)))

sums = np.sum(flux, axis=1)
flux_norm = flux / sums[:, np.newaxis]
means = np.mean(flux_norm, axis=1)
flux_res = flux_norm - means[:, np.newaxis]

# print(sums.shape)
# print(flux_res.shape)

index = 2000
fig, axs = plt.subplots(2, dpi=200)

axs[0].plot(logwave, flux[index])
axs[0].set_xlabel(r'$\log_{10}\lambda$ ($\lambda$ in $\mathrm{\AA}$)')
axs[0].set_ylabel('flux')

axs[1].plot(wave, flux_res[index])
axs[1].set_xlabel(r'$\lambda$ ($\mathrm{\AA}$)')
axs[1].set_ylabel('flux residue')

plt.figtext(0.5, -0.05, r'flux and flux residue in $10^{-17} \ \mathrm{erg} \ \mathrm{s}^{-1} \ \mathrm{cm}^{-2} \ \mathrm{\AA}^{-1}$', ha='center')
fig.suptitle(f'galaxy number {index}')
fig.tight_layout()
plt.savefig('ps6-1abc.png', bbox_inches='tight')
plt.show()

# a = np.arange(1, 10)
# i = np.arange(1, 6)
# print(a[i])


# (d)
cov = np.dot(flux_res.T, flux_res)
print('cov.shape =', cov.shape)

# ev1, evec1 = eigen1(cov)
# np.save('ev1.npy', ev1)
# np.save('evec1.npy', evec1)
ev1 = np.load('ev1.npy')
evec1 = np.load('evec1.npy')
print('first five ev1s:', ev1[np.arange(0, 6)])

fig, ax = plt.subplots(dpi=200)
ax.plot(wave, evec1[:, 0], label='evec 1')
ax.plot(wave, evec1[:, 1], label='evec 2')
ax.plot(wave, evec1[:, 2], label='evec 3')
ax.plot(wave, evec1[:, 3], label='evec 4')
ax.plot(wave, evec1[:, 4], label='evec 5')
ax.legend()
ax.set_xlabel(r'$\lambda$ ($\mathrm{\AA}$)')
ax.set_ylabel('eigenvector components')
ax.set_title('First five eigenvectors')

fig.tight_layout()
plt.savefig('ps6-1d1.png', bbox_inches='tight')
plt.show()

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']

fig, axs = plt.subplots(nrows=5, sharex=True, dpi=200, figsize=(6, 10))
axs[0].plot(wave, evec1[:, 0], color=colors[0], label='evec 1')
axs[0].legend()
axs[1].plot(wave, evec1[:, 1], color=colors[1], label='evec 2')
axs[1].legend()
axs[2].plot(wave, evec1[:, 2], color=colors[2], label='evec 3')
axs[2].legend()
axs[3].plot(wave, evec1[:, 3], color=colors[3], label='evec 4')
axs[3].legend()
axs[4].plot(wave, evec1[:, 4], color=colors[4], label='evec 5')
axs[4].legend()
fig.supxlabel(r'$\lambda$ ($\mathrm{\AA}$)')
fig.supylabel('eigenvector components')
fig.suptitle('First five eigenvectors')

fig.tight_layout()
plt.savefig('ps6-1d2.png', bbox_inches='tight')
plt.show()


# (e)
# ev2, evec2 = eigen2(flux_res)
# np.save('ev2.npy', ev2)
# np.save('evec2.npy', evec2)
ev2 = np.load('ev2.npy')
evec2 = np.load('evec2.npy')
print('first five ev2s:', ev2[np.arange(0, 6)])

fig, ax = plt.subplots(dpi=200)
ax.plot(wave, evec2[:, 0], label='evec 1')
ax.plot(wave, evec2[:, 1], label='evec 2')
ax.plot(wave, evec2[:, 2], label='evec 3')
ax.plot(wave, evec2[:, 3], label='evec 4')
ax.plot(wave, evec2[:, 4], label='evec 5')
ax.legend()
ax.set_xlabel(r'$\lambda$ ($\mathrm{\AA}$)')
ax.set_ylabel('eigenvector components')
ax.set_title('First five eigenvectors computed using SVD')

fig.tight_layout()
plt.savefig('ps6-1e1.png', bbox_inches='tight')
plt.show()

fig, axs = plt.subplots(nrows=5, sharex=True, dpi=200, figsize=(6, 10))
axs[0].plot(wave, evec2[:, 0], color=colors[0], label='evec 1')
axs[0].legend()
axs[1].plot(wave, evec2[:, 1], color=colors[1], label='evec 2')
axs[1].legend()
axs[2].plot(wave, evec2[:, 2], color=colors[2], label='evec 3')
axs[2].legend()
axs[3].plot(wave, evec2[:, 3], color=colors[3], label='evec 4')
axs[3].legend()
axs[4].plot(wave, evec2[:, 4], color=colors[4], label='evec 5')
axs[4].legend()
fig.supxlabel(r'$\lambda$ ($\mathrm{\AA}$)')
fig.supylabel('eigenvector components')
fig.suptitle('First five eigenvectors computed using SVD')

fig.tight_layout()
plt.savefig('ps6-1e2.png', bbox_inches='tight')
plt.show()

t1 = timeit.timeit('eigen1(cov)', globals=globals(), number=2)
t2 = timeit.timeit('eigen2(flux_res)', globals=globals(), number=2)
print('t1 =', t1)
print('t2 =', t2)


# (f)
u, w, vt = np.linalg.svd(cov)
print('condition number of cov:', np.max(w) / np.min(w))
u, w, vt = np.linalg.svd(flux_res)
print('condition number of flux_res:', np.max(w) / np.min(w))


# (g)
Nc = 5
basis = evec2[:, :Nc]
coeff = np.dot(flux_res, basis)
approx_res = np.dot(coeff, basis.T)
approx_flux = (means[:, np.newaxis] + approx_res) * sums[:, np.newaxis]

index = 2000
fig, axs = plt.subplots(2, sharex=True, dpi=200)
axs[0].plot(wave, flux[index], color=colors[0], label='flux')
axs[0].legend()
axs[1].plot(wave, approx_flux[index], color=colors[1], label='approximated flux')
axs[1].legend()
fig.supxlabel(r'$\lambda$ ($\mathrm{\AA}$)')
fig.supylabel('flux\n' + r'($10^{-17} \ \mathrm{erg} \ \mathrm{s}^{-1} \ \mathrm{cm}^{-2} \ \mathrm{\AA}^{-1}$)', multialignment='center')
fig.suptitle(rf'Approximated flux with $N_c$ = {Nc} for galaxy number {index}')

fig.tight_layout()
plt.savefig('ps6-1g.png', bbox_inches='tight')
plt.show()


# (h)
fig, axs = plt.subplots(2, dpi=200)
axs[0].scatter(coeff[:, 0], coeff[:, 1], s=5)
axs[0].set_xlabel(r'$c_0$')
axs[0].set_ylabel(r'$c_1$')
axs[1].scatter(coeff[:, 0], coeff[:, 2], s=5)
axs[1].set_xlabel(r'$c_0$')
axs[1].set_ylabel(r'$c_2$')
fig.suptitle('First three coefficients')

fig.tight_layout()
plt.savefig('ps6-1h.png', bbox_inches='tight')
plt.show()


# (i)
Ncs = np.arange(1, 21)
rms = np.zeros(Ncs.shape)
for Nc in Ncs:
    basis = evec2[:, :Nc]
    # print(basis.shape)
    coeff = np.dot(flux_res, basis)
    approx_res = np.dot(coeff, basis.T)
    approx_flux = (means[:, np.newaxis] + approx_res) * sums[:, np.newaxis]
    
    rms[Nc -1] = np.sqrt(np.mean(np.square(flux - approx_flux)))

fig, ax = plt.subplots(dpi=200)
ax.plot(Ncs, rms)
ax.set_xlabel(r'$N_c$')
ax.set_ylabel('rms\n' + r'($10^{-17} \ \mathrm{erg} \ \mathrm{s}^{-1} \ \mathrm{cm}^{-2} \ \mathrm{\AA}^{-1}$)', multialignment='center')
ax.set_title('Root mean square error')

fig.tight_layout()
plt.savefig('ps6-1i.png', bbox_inches='tight')
plt.show()

print('rms (Nc=20):', rms[19])

