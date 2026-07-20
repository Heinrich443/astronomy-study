import numpy as np

a = np.array([[10, 20],
              [30, 40]])
b = np.arange(4).reshape(2, 2)

print(a)
print(b)

c_dot = np.dot(a, b)
print(c_dot)
c_dot_2 = a.dot(b)
print(c_dot_2)

d = np.random.random((2, 4))
print(d)
print(np.sum(d))
print(np.max(d))
print(np.min(d))
print(np.min(d, axis=0))
print(np.min(d, axis=1))

e = np.arange(3, 27, 2).reshape((3, 4))
# e = np.array([1, 3, 2, 5, 0, 7])
# e = np.array([[1, 3, 2, 5, 0, 7],
#               [5, 2, 6, 1, 8, 0]])

print(e)

# index of minimum
print(np.argmin(e))
print(e.argmin())
# index of maximum
print(np.argmax(e))
print(e.argmax())
# average of elements
print(np.mean(e))
print(e.mean())
print(np.average(e))
# median
print(np.median(e))

print(np.cumsum(e))

print(np.diff(e))

print(np.nonzero(e))

print(np.sort(e))

print(np.transpose(e))
print(e.T)

print(np.clip(e, 5, 9))