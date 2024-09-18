import numpy as np

def quadratic_std(a, b, c):
    x1 = np.float64((- b + np.sqrt(np.square(b) - 4 * a * c)) / (2 * a))
    x2 = np.float64((- b - np.sqrt(np.square(b) - 4 * a * c)) / (2 * a))
    return x1, x2

def quadratic_alt(a, b, c):
    x1 = np.float64((2 * c) / (- b - np.sqrt(np.square(b) - 4 * a * c)))
    x2 = np.float64((2 * c) / (- b + np.sqrt(np.square(b) - 4 * a * c)))
    return x1, x2

def quadratic(a, b, c):
    v1 = np.abs(np.float64((- b + np.sqrt(np.square(b) - 4 * a * c))))
    v2 = np.abs(np.float64((- b - np.sqrt(np.square(b) - 4 * a * c))))
    
    if v1 > (np.abs(b) / 10):
        x1 = np.float64((- b + np.sqrt(np.square(b) - 4 * a * c)) / (2 * a))
    else:
        x1 = np.float64((2 * c) / (- b - np.sqrt(np.square(b) - 4 * a * c)))
        
    if v2 > (np.abs(b) / 10):
        x2 = np.float64((- b - np.sqrt(np.square(b) - 4 * a * c)) / (2 * a))
    else:
        x2 = np.float64((2 * c) / (- b + np.sqrt(np.square(b) - 4 * a * c)))
        
    return x1, x2
    

x1, x2 = quadratic_std(0.001, -1000, 0.001)
print(x1, x2)

x1, x2 = quadratic_alt(0.001, -1000, 0.001)
print(x1, x2)

x1, x2 = quadratic(0.001, -1000, 0.001)
print(x1, x2)