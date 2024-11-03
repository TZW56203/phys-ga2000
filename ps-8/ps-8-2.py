import numpy as np
import matplotlib.pyplot as plt

piano = np.loadtxt('piano.txt')
trumpet = np.loadtxt('trumpet.txt')

size = piano.size
s = 44100  # samples per second
f1 = 1 / (size * 1 / s)
# print(f1)

# piano
fig, ax = plt.subplots(dpi=200)
ax.plot(piano)
ax.set_xlabel(rf'$t$ (1/{s} s)')
ax.set_ylabel('waveform')
ax.set_title('piano')

fig.tight_layout()
plt.savefig('ps-8-2p.png')
plt.show()

# trumpet
fig, ax = plt.subplots(dpi=200)
ax.plot(trumpet)
ax.set_xlabel(rf'$t$ (1/{s} s)')
ax.set_ylabel('waveform')
ax.set_title('trumpet')

fig.tight_layout()
plt.savefig('ps-8-2t.png')
plt.show()

# piano and trumpet
fig, ax = plt.subplots(dpi=200)
ax.plot(np.arange(10000, 10500), piano[10000:10500], label='piano')
ax.plot(np.arange(10000, 10500), trumpet[10000:10500], label='trumpet')
ax.legend()
ax.set_xlabel(rf'$t$ (1/{s} s)')
ax.set_ylabel('waveform')
ax.set_title('piano & trumpet')

fig.tight_layout()
plt.savefig('ps-8-2pt.png')
plt.show()

FTpiano = np.fft.rfft(piano)
FTtrumpet = np.fft.rfft(trumpet)

# cutoff = 10000
# fig, ax = plt.subplots(dpi=200)
# ax.plot(np.abs(FTpiano[:cutoff]), label='piano')
# ax.plot(np.abs(FTtrumpet[:cutoff]), label='trumpet')
# ax.legend()
# ax.set_xlabel(rf'$f$ ({f1} Hz)')
# ax.set_ylabel('coefficient')
# ax.set_title(f'First {cutoff} Fourier coeffients')

# fig.tight_layout()
# plt.show()

cutoff = 10000
f = np.arange(cutoff) * f1

#FT piano
fig, axs = plt.subplots(2, figsize=(4, 5), dpi=200)
axs[0].plot(np.abs(FTpiano[:cutoff]))
axs[0].set_xlabel(rf'$f$ ({f1} Hz)')
axs[1].plot(f , np.abs(FTpiano[:cutoff]))
axs[1].set_xlabel(r'$f$ (Hz)')
fig.supylabel('coefficient')
fig.suptitle(f'First {cutoff} Fourier coeffients for piano')

fig.tight_layout()
plt.savefig('ps-8-2FTp.png')
plt.show()

#FT trumpet
fig, axs = plt.subplots(2, figsize=(4, 5), dpi=200)
axs[0].plot(np.abs(FTtrumpet[:cutoff]))
axs[0].set_xlabel(rf'$f$ ({f1} Hz)')
axs[1].plot(f , np.abs(FTtrumpet[:cutoff]))
axs[1].set_xlabel(r'$f$ (Hz)')
fig.supylabel('coefficient')
fig.suptitle(f'First {cutoff} Fourier coeffients for trumpet')

fig.tight_layout()
plt.savefig('ps-8-2FTt.png')
plt.show()

print('piano frequencies where the coefficients > 7e7:')
print(np.nonzero(np.abs(FTpiano) > 7e7)[0] * f1)
print('trumpet frequencies where the coefficients > 5e7:')
print(np.nonzero(np.abs(FTtrumpet) > 5e7)[0] * f1)