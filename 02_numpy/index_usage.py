import numpy as np

a = np.arange(3, 15).reshape((3, 4))
print(a)
print(a[2])
print(a[1][2])
print(a[1, 2])
print(a[:, 2])  # column 2
print(a[1, :])  # row 1
print(a[1, 1:3])

print(a.flatten())
for item in a.flat:
    print(item, end=" ")
print()

