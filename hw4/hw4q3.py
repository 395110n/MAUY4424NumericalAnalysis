import numpy as np

def powerMethod(A, threshold):
    vk1 = np.random.random(size=A.shape[0])
    vk2 = np.random.random(size=A.shape[0])
    it = 0
    while 1:

        vk1 = vk2 / np.linalg.norm(vk2)
        vk2 = A @ vk1
        vk2 = vk2 / np.linalg.norm(vk2)

        Avk2 = A @ vk2
        Avk1 = A @ vk1
        lambda2 = np.dot(vk2, Avk2)
        lambda1 = np.dot(vk1, Avk1)
        
        print(f"iteration: {it}, diff: {abs(lambda1 - lambda2)}")
        if abs(lambda1 - lambda2) < threshold:
            return vk2, lambda2, it
        it += 1

itPower = []
for num in range (100):
    size = 100
    A = np.random.uniform(low=-10, high=100, size=(size, size))
    # A = A.T @ A
    # this step is to ensure that we don't get complex eigenvalues 
    eigenvalues = np.linalg.eigvals(A)
    v, lamda, it = powerMethod(A, 0.00001)
    itPower.append(it)
    max_eigenvalue = np.max(eigenvalues)
itPowernp = np.array(itPower)
avgPower = np.mean(itPower)


def inversePowerMethod(A, threshold):
    vk1 = np.random.random(size=A.shape[0])
    vk2 = np.random.random(size=A.shape[0])
    vk1 = vk1 / np.linalg.norm(vk1)
    vk2 = vk2 / np.linalg.norm(vk2)
    it = 0
    alpha = np.linalg.norm(A)
    B = A - alpha * np.identity(A.shape[0])
    while 1:
        vk1 = vk2
        vk2 = np.linalg.solve(B, vk1)
        vk2 = vk2 / np.linalg.norm(vk2)
        
        lambda2 = np.dot(vk2, A @ vk2)
        lambda1 = np.dot(vk1, A @ vk1)
        B = A - lambda2 * np.identity(A.shape[0])
        it += 1

        print(f"iteration: {it}, diff: {abs(lambda1 - lambda2)}")
        if abs(lambda1 - lambda2) < threshold:
            return vk2, lambda2, it

itInverse = 0
for num in range(100):
    size = 100
    A = np.random.uniform(low=-10, high=100, size=(size, size))
    v, lamda, it= inversePowerMethod(A, 0.00001)
    itInverse += it
    eigenvalues = np.linalg.eigvals(A)
    max_eigenvalue = np.max(eigenvalues)
avgInverse = itInverse / 100

print(f"avg Power: {avgPower}, avg Inverse: {avgInverse}")
