import numpy as np
import timeit

# Exercise 2.9: The Madelung Constant

def M_loop(L):
    M = np.float32(0)
    r = np.arange(-L, L+1)
    
    for i in r:
        for j in r:
            for k in r:
                if not (i == 0 and j == 0 and k == 0):
                    M += np.float32(np.power(-1, np.abs(i + j + k)) / np.sqrt(np.square(i) + np.square(j) + np.square(k)))
                    
    return M


def M_mesh(L):
    r = np.arange(-L, L+1, dtype = np.float32)
    i, j, k = np.meshgrid(r, r, r)
    
    M = np.power(-1, np.abs(i + j + k)) * np.sqrt(np.square(i) + np.square(j) + np.square(k))
    M = 1/M[M != 0]
    
    return np.sum(M, dtype=np.float32)

L = 50


print('The Madelung constant computed using for loop is')
time1 = timeit.default_timer()
print(M_loop(L))
time2 = timeit.default_timer()

print('The Madelung constant computed without using for loop is')
time3 = timeit.default_timer()
print(M_mesh(L))
time4 = timeit.default_timer()

print('\n')
print('The time using for loop is')
print(time2 - time1, 'second')
print('The time without using for loop is')
print(time4 - time3, 'second')
print('\n')

if (time2 - time1) < (time4 - time3):
    print('The function using for loop is faster')

else:
    print('The function without using for loop is faster')

# The true value is -1.747565