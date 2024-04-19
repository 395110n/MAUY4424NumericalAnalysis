import numpy as np

def find_U_b(A, b):
    dim = A.shape[0]
    for i in range(dim - 1):
        maxInd = np.argmax(A[i:, i])
        A[[i, i + maxInd], :] = A[[i + maxInd, i], :]
        b[i], b[i + maxInd] = b[i + maxInd], b[i]
        for j in range(1, dim - i):
            L = A[i + j, i] / A[i, i]
            A[i + j, i:] -= L * A[i, i:]
            b[i + j] -= L * b[i] 
    return A, b

def find_x(A, b):
    dim = A.shape[0]
    x = np.zeros(dim)
    for i in range(dim - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:]))/ A[i,i]
    return x

A = np.random.uniform(low= -10, high=10, size=(100, 10))
b = np.random.uniform(low = -10, high = 10, size=(100))
ATA = A.transpose() @ A
ATA_new , b_new = find_U_b(ATA, b)
x = find_x(ATA_new, b_new)
print(x)
print(A @ x)
print(b)