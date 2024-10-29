import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def y(x):
    return np.square(x - 0.3) * np.exp(x)

def f(x):
    return((x-1.1)**2)

def parabolic_step(func=None, a=None, b=None, c=None):
    """returns the minimum of the function as approximated by a parabola"""
    fa = func(a)
    fb = func(b)
    fc = func(c)
    denom = (b - a) * (fb - fc) - (b - c) * (fb - fa)
    numer = (b - a)**2 * (fb - fc) - (b - c)**2 * (fb - fa)
    # If singular, just return b 
    if(np.abs(denom) < 1.e-15):
        x = b
    else:
        x = b - 0.5 * numer / denom
    return(x)

def parabolic_minimize(func=None, astart=None, bstart=None, cstart=None, tol=1.e-5, maxiter=10000):
    a = astart
    b = bstart
    c = cstart
    bold = b + 2. * tol
    niter = 0
    while((np.abs(bold - b) > tol) and (niter < maxiter)):
        bold = b
        b = parabolic_step(func=func, a=a, b=b, c=c)
        if(b < bold):
            c = bold
        else:
            a = bold
        niter = niter + 1
    return(b)

def golden(func=None, astart=None, bstart=None, cstart=None, tol=1.e-5, maxiter=10000):
    gsection = (3. - np.sqrt(5)) / 2
    a = astart
    b = bstart
    c = cstart
    niter = 0
    while((np.abs(c - a) > tol) and (niter < maxiter)):
        # Split the larger interval
        if((b - a) > (c - b)):
            x = b
            b = b - gsection * (b - a)
        else:
            x = b + gsection * (c - b)
        fb = func(b)
        fx = func(x)
        if(fb < fx):
            c = x
        else:
            a = b
            b = x
        niter = niter + 1
    return(b)
    
def MyBrentMin(func=None, astart=None, bstart=None, cstart=None, tol=1.e-5, maxiter=10000):
    a = astart
    b = bstart
    c = cstart
    bold = b + 2. * tol
    boldold = c + 1
    OK = True
    
    niter = 0
    while((np.abs(bold - b) > tol) and (niter < maxiter)):
        bold = b
        b = parabolic_step(func=func, a=a, b=b, c=c)
        if (b < a or b > c or b > boldold):
            OK = False
        if(b < bold):
            c = bold
        else:
            a = bold
        boldold = bold
        niter = niter + 1
        # print(a, b, c)
    # print('OK =', OK)
    if OK:
        return(b)
    else:
        return golden(func=func, astart=astart, bstart=bstart, cstart=cstart, tol=tol, maxiter=maxiter)

astart = -2
bstart = 0
cstart = 2

MyMin = MyBrentMin(func=y, astart=astart, bstart=bstart, cstart=cstart)
scipyMin = optimize.brent(y)
ParaMin = parabolic_minimize(func=y, astart=astart, bstart=bstart, cstart=cstart)
GoldMin = golden(func=y, astart=astart, bstart=bstart, cstart=cstart)

# print(f'astart = {astart}, bstart = {bstart}, cstart = {cstart}')
print('MyMin:', MyMin)
print('scipyMin:', scipyMin)
# print('ParaMin:', ParaMin)
# print('GoldMin:', GoldMin)
print('MyMin - scipyMin:', MyMin - scipyMin)

xs = np.arange(-2, 2.01, 0.01)
fig, ax = plt.subplots(dpi=200)
ax.plot(xs, y(xs))
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y(x)$')

fig.tight_layout()
plt.savefig('ps-7-2.png')
plt.show()


