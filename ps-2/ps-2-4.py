import numpy as np
import matplotlib.pyplot as plt

# Exercise 3.7: The Mandelbrot set

N = 1000
iterations = 100

def myplot():
    r = np.linspace(-2, 2, num=N, dtype=np.float32)
    
    re, im = np.meshgrid(r, r)
    c = re + im * 1j
    z = np.zeros((N, N), dtype=np.complex64)
    
    for i in np.arange(iterations):
        z = np.where(np.abs(z) <= 2, np.square(z) + c, z)
    
    z = np.where(np.abs(z) <= 2, 1, 0)
    
    fig, ax = plt.subplots(figsize=(6, 6), dpi=300)
    # ax.set_axis_off()
    ax.imshow(z, origin='lower')
    ax.set_xlabel('Re(c)')
    ax.set_ylabel('Im(c)')
    ax.set_xticks(np.arange(0, 1250, 250), np.arange(-2, 3, 1))
    ax.set_yticks(np.arange(0, 1250, 250), np.arange(-2, 3, 1))
    plt.savefig('Mandelbrot-set.png')
    plt.show()

myplot()