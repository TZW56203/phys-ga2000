import numpy as np
import matplotlib.pyplot as plt
import timeit


def mydot(A, B):
    N = A.shape[0]
    C = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    
    return C


# seed = 12345
# rng = np.random.default_rng(seed)
rng = np.random.default_rng()

num_dot = 30
num_loop = 10


# dot
N_dot = np.arange(100, 1100, 100)
t_dot = np.zeros(N_dot.shape)

# test
A = np.identity(3)
B = np.ones((3, 3))
print('A * B =', np.dot(A, B))

for i, N in enumerate(N_dot):
    A = 2 * rng.random((N, N), dtype = np.float64) - 1
    B = 2 * rng.random((N, N), dtype = np.float64) - 1
    
    t_dot[i] = timeit.timeit('np.dot(A, B)', globals=globals(), number=num_dot)
    

# loop
N_loop = np.arange(10, 110, 10)
t_loop = np.zeros(N_loop.shape)

# test
A = np.identity(3)
B = np.ones((3, 3))
print('A * B =', mydot(A, B))

for i, N in enumerate(N_loop):
    A = 2 * rng.random((N, N), dtype = np.float64) - 1
    B = 2 * rng.random((N, N), dtype = np.float64) - 1
    
    t_loop[i] = timeit.timeit('mydot(A, B)', globals=globals(), number=num_loop)


# plot
fig, axs = plt.subplots(2)

axs[0].plot(N_loop, t_loop / num_loop)
axs[0].set_xlabel('N')
axs[0].set_ylabel('time (s)')
axs[0].set_title('loop')

axs[1].plot(N_dot, t_dot / num_dot)
axs[1].set_xlabel('N')
axs[1].set_ylabel('time (s)')
axs[1].set_title('dot')

fig.tight_layout()
plt.savefig('t-N.png')
plt.show()


c_loop = np.round(np.polyfit(np.log(N_loop), np.log(t_loop / num_loop), 1), 2)
c_dot = np.round(np.polyfit(np.log(N_dot), np.log(t_dot / num_dot), 1), 2)

eqn_loop = f'y = {c_loop[0]}x + ({c_loop[1]})'
eqn_dot = f'y = {c_dot[0]}x + ({c_dot[1]})'

fig, axs = plt.subplots(2)

axs[0].plot(np.log(N_loop), np.log(t_loop / num_loop), label = eqn_loop)
axs[0].legend()
axs[0].set_xlabel('ln(N)')
axs[0].set_ylabel('ln(t)')
axs[0].set_title('loop')

axs[1].plot(np.log(N_dot), np.log(t_dot / num_dot), label = eqn_dot)
axs[1].legend()
axs[1].set_xlabel('ln(N)')
axs[1].set_ylabel('ln(t)')
axs[1].set_title('dot')

fig.tight_layout()
plt.savefig('lnt-lnN.png')
plt.show()




