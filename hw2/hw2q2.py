import numpy as np

def get_lower_triangular_inverse (L):
    Linverse = np.zeros(L.shape)

    for j in range(L.shape[0]):
        for i in range(L.shape[0]):
            if i == j:
                Linverse[i, j] = (1 - np.dot(L[i, j:i], Linverse[j:i, j])) / L[i, i]
            else:
                Linverse[i, j] = ( - np.dot(L[i, j:i], Linverse[j:i, j])) / L[i, i]
    return Linverse

dim = 5
L = np.tril(np.random.randint(-10, 10, size=(dim, dim)), k=0)
print(L)

Linverse = get_lower_triangular_inverse(L)
print(Linverse)

print(L@Linverse)