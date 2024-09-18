import numpy as np


# np.float32 precision
x = np.float32(1)
y = np.float32(np.exp2(-23))
z = np.float32(1.01 * np.exp2(-24))
a = np.float32(np.exp2(-24))

print('In np.float32 precision, the smallest number you can add to 1 and get an answer that is different than 1 is approximately')
print('2^-23 or anything larger than 2^-24', '\n')
print('For example')
print('1 + 2^-23 =', np.float32(x + y))
print('1 + 1.01 * 2^-24 =', np.float32(x + z))
print('1 + 2^-24 =', np.float32(x + a), '\n')


# np.float64 precision
x = np.float64(1)
y = np.float64(np.exp2(-52))
z = np.float64(1.01 * np.exp2(-53))
a = np.float64(np.exp2(-53))

print('In np.float64 precision, the smallest number you can add to 1 and get an answer that is different than 1 is approximately')
print('2^-52 or anything larger than 2^-53', '\n')

print('For example')
print('1 + 2^-52 =', np.float64(x + y))
print('1 + 1.01 * 2^-53 =', np.float64(x + z))
print('1 + 2^-53 =', np.float64(x + a), '\n')


# np.float32 precision
min32 = np.float32((0 + np.exp2(-23)) * np.exp2(-126))
max32 = np.float32((1 + (1 - np.exp2(-23))) * np.exp2(127))
print('In np.float32, the minimum (positive) number is approximately')
print(min32)
print('In np.float32, the maximum (positive) number is approximately')
print(max32, '\n')

# np.float64 precision
min64 = np.float64((0 + np.exp2(-52)) * np.exp2(-1022))
max64 = np.float64((1 + (1 - np.exp2(-52))) * np.exp2(1023))
print('In np.float64, the minimum (positive) number is approximately')
print(min64)
print('In np.float64, the maximum (positive) number is approximately')
print(max64, '\n')

print('check')
print(
      np.finfo(np.float32).eps,
      np.finfo(np.float32).tiny, # smallest normal number
      np.finfo(np.float32).min,
      np.finfo(np.float32).max
      )


print(
      np.finfo(np.float64).eps,
      np.finfo(np.float64).tiny, # smallest normal number
      np.finfo(np.float64).min,
      np.finfo(np.float64).max
      )