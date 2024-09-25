import numpy as np
import matplotlib.pyplot as plt
# import scipy.stats as stats

def std_normal(x):
    ans = 1 / np.sqrt(2 * np.pi) * np.exp(-np.square(x) / 2)
    return ans

seed = 12345
rng = np.random.default_rng(seed)

M = 10000
N_test = 10000
N_array = np.arange(1, 1001, 20)


x = rng.exponential(size=(N_test, M))
y = np.sum(x, axis=0) / N_test
z = np.sqrt(N_test) * (y - 1)

x_gauss = np.linspace(-5, 5, 100)
y_gauss = std_normal(x_gauss)

fig, ax = plt.subplots()
ax.hist(y, bins=20)
ax.set_xlabel('y')
ax.set_title(f'histogram of y with N = {N_test}, M = {M}')
plt.savefig('ps-3-4-yhist.png')
plt.show()

fig, ax = plt.subplots()
ax.hist(z, bins=20, density=True)
ax.plot(x_gauss, y_gauss)
ax.set_xlabel('z')
ax.set_title(f'histogram of z with N = {N_test}, M = {M}')
plt.savefig('ps-3-4-zhist.png')
plt.show()


M = 10000

mean = np.zeros(N_array.shape)
variance = np.zeros(N_array.shape)
std = np.zeros(N_array.shape)
skewness = np.zeros(N_array.shape)
kurtosis = np.zeros(N_array.shape)

# =============================================================================
# mean2 = np.zeros(N_array.shape)
# variance2 = np.zeros(N_array.shape)
# std2 = np.zeros(N_array.shape)
# skewness2 = np.zeros(N_array.shape)
# kurtosis2 = np.zeros(N_array.shape)
# =============================================================================


for i, N in enumerate(N_array):
    x = rng.exponential(size=(N, M))
    y = np.sum(x, axis=0) / N
    
    mean[i] = np.sum(y) / M
    variance[i] = np.sum(np.square(y - mean[i])) / M
    std[i] = np.sqrt(variance[i])
    skewness[i] = np.sum(np.power((y - mean[i]) / std[i], 3)) / M
    kurtosis[i] = np.sum(np.power((y - mean[i]) / std[i], 4)) / M - 3
    
# =============================================================================
#     mean2[i] = np.mean(y)
#     variance2[i] = np.var(y)
#     skewness2[i] = stats.skew(y, bias=False)
#     kurtosis2[i] = stats.kurtosis(y, bias=False)
# =============================================================================


fig, axs = plt.subplots(4, figsize=(10, 15))

axs[0].plot(N_array, mean)
axs[0].set_title('mean')

axs[1].plot(N_array, variance)
axs[1].set_title('variance')

axs[2].plot(N_array, skewness)
axs[2].set_title('skewness')
axs[2].hlines(y=0, xmin=0, xmax=1000, color = 'r')

axs[3].hlines(y=0, xmin=0, xmax=1000, color = 'r')
axs[3].plot(N_array, kurtosis)
axs[3].set_title('kurtosis')
axs[3].set_xlabel('N')

fig.suptitle(f'moments of y vs N with M = {M}')
fig.tight_layout()
plt.savefig('ps-3-4_moments.png')
plt.show()


# =============================================================================
# fig, axs = plt.subplots(4, figsize=(10, 15))
# 
# axs[0].plot(N_array, mean2)
# axs[0].set_title('mean')
# 
# axs[1].plot(N_array, variance2)
# axs[1].set_title('variance')
# 
# axs[2].plot(N_array, skewness2)
# axs[2].set_title('skewness')
# axs[2].hlines(y=0, xmin=0, xmax=1000, color = 'r')
# 
# axs[3].hlines(y=0, xmin=0, xmax=1000, color = 'r')
# axs[3].plot(N_array, kurtosis2)
# axs[3].set_title('kurtosis')
# axs[3].set_xlabel('N')
# 
# fig.suptitle(f'moments of y vs N with M = {M}')
# fig.tight_layout()
# plt.savefig('ps-3-4_moments-2.png')
# plt.show()
# =============================================================================

