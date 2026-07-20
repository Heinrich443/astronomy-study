import numpy as np

array = np.array([[1, 2, 3],
                  [2, 3, 4]])

print('dimension: ', array.ndim)
print('shape: ', array.shape)
print('size: ', array.size)

a = np.array([1, 2, 3], dtype=np.int64)
print(a)
print(a.dtype)  # data type

b = np.array([[1.2, 2, 3],
              [4, 5, 6]], dtype=np.float64)
print(b)
print(b.dtype)

zeros = np.zeros((2, 3))
print(zeros)
print(zeros.dtype)

ones = np.ones((3, 4))
# ones = np.ones((3, 4), dtype=np.int64)
print(ones)
print(ones.dtype)

empty = np.empty((2, 2))
print(empty)
print(empty.dtype)

range = np.arange(10, 20, 2)
print(range)
print(range.dtype)

range = np.arange(2.3, 5.3, 0.5)
print(range)
print(range.dtype)

range = np.arange(12).reshape((3, 4))
print(range)
print(range.dtype)

line = np.linspace(1, 10, 5)
print(line)

line = np.linspace(1, 10, 6).reshape((3, 2))
print(line)