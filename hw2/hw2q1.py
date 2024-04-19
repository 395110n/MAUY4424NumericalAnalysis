import numpy as np

def LU_factor(A):
    L, U = np.zeros(A.shape), np.zeros(A.shape)   
    #set L, U to be square matrices with the same dimension as A

    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            #calculate U first to avoid division by zero
            if (i <= j):
                U[i, j] = A[i, j] - np.dot(L[i, 0:i], U[0:i, j])


            if (j <= i):   
                L[i, j] = (A[i, j] - np.dot(L[i, :j],U[:j, j]))/U[j, j]  

    return L, U

A = np.random.uniform(-5, 5, (100, 100))

L, U = LU_factor(A)
print(U[0, :] == A[0, :])






        


        


