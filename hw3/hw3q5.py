import numpy as np 

size = (200, 100)
A = np.random.uniform(low = -10, high=10, size = size)
Q = np.zeros(shape=size)
R = np.zeros(shape = (size[1], size[1]))
Qr, Rr = np.linalg.qr(A)

for col in range(size[1]):
    Qk = Q[:, :col]
    Qtk = Qk.transpose()
    Acol = A[:, col].reshape(-1, 1)
    res = Qtk @ Acol
    diff = Qtk * res
    sum = np.sum(diff, axis = 0).reshape(-1, 1)
    v = Acol - sum
    norm = np.linalg.norm(v)
    q = (v / norm).flatten()
    Q[:, col] = q
    result = np.zeros(size[1])
    result[:len(res)] = res.flatten()
    result[col] = norm
    R[:, col] = result

print(Q @ R)
print(A)

print(Q @ Q.transpose())
