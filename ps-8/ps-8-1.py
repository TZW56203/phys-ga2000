import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

age, reco = np.loadtxt('survey.csv', delimiter=',', skiprows=1, unpack='true')

def logistic(b, a):
    return 1. / (1 + np.exp(-(b[0] + b[1] * a)))

def likely(b, a, r):
    return - np.sum(r * np.log(logistic(b, a)) + (1 - r) * np.log(1 - logistic(b, a)))

res = minimize(likely, (-5, .1), args=(age, reco))
print(res)

print('\n')
print('beta_0, beta_1:', res.x)
print('Errors:', np.sqrt(np.diag(res.hess_inv)))
print('Covariance matrix:')
print(res.hess_inv)

xs = np.arange(100)
fig, ax = plt.subplots(dpi=200)
ax.plot(age, reco, '.', label='survey results')
ax.plot(xs, logistic(res.x, xs), label='logistic model')
ax.legend()
ax.set_xlabel('age')
ax.set_ylabel('recognize')
ax.set_title('Survey results and logistic model')

fig.tight_layout()
plt.savefig('ps-8-1.png')
plt.show()