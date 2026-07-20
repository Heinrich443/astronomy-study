import numpy as np

a = np.arange(4)
b = a
c = a
d = b

print(b is a)
print(d is a)

b = a.copy()    # deep copy
print(b is a)