import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

C = np.vstack((A, B))   # vertical stack
D = np.hstack((A, B, B))   # horizontal stack

print(A, A.shape)
print(B, B.shape)
print(C, C.shape)
print(D, D.shape)

E = A[np.newaxis, :]
F = A[:, np.newaxis]
print(E, E.shape)
print(F, F.shape)

A = A[:, np.newaxis]
B = B[:, np.newaxis]
# G = np.hstack((A, B, B))
G = np.concatenate((A, B, B, A), axis=0)
# G = np.concatenate((A, B, B, A), axis=1)
print(A)
print(B)
print(G)
