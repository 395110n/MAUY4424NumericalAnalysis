import numpy as np
import matplotlib.pyplot as plt

def L(val, k, x):
    xk = x[k]
    x_not_k = np.delete(x, k)
    over = val - x_not_k
    under = xk - x_not_k
    res = np.prod(over / under)
    return res

def LPrime(val, k, x, epsilon=1e-6):
    xk = x[k]
    xInter = np.delete(x, k)
    coeff = 1 / (xk - xInter)
    vals = np.zeros(xInter.shape)
    for j in range(vals.shape[0]):
        xInter2 = np.delete(xInter, j)
        over = val - xInter2
        under = xk - xInter2
        vals[j] = np.prod(over / under)
    res = np.dot(coeff, vals)
    return res
    # return (L(val + epsilon, k, x) - L(val, k, x)) / epsilon

# def derivative(func, x, epsilon=1e-8):
#     return (func(x + epsilon) - func(x)) / epsilon

def Hk(val, k, x):
    return (L(val, k, x) ** 2) * (1 - 2*LPrime(x[k], k, x) * (val - x[k]))

def Kk(val, k, x):
    return (L(val, k, x) ** 2) * (val - x[k])

def P2nPlus1(val, x, y, z):
    outterRes = np.zeros(val.shape)
    for i in range(val.shape[0]):
        res = np.zeros(x.shape)
        for k in range(x.shape[0]):
            res[k] = Hk(val[i], k, x) * y[k] + Kk(val[i], k, x) * z[k]

        outterRes[i] = res.sum()
    return outterRes

def derivativeTanh(x):
    return 1 - np.power(np.tanh(x), 2)

x = np.arange(21)

y = np.tanh(x)

z = derivativeTanh(x)

testX = np.arange(0, 21, 0.5)
trueY = np.tanh(testX)
print(trueY)
myY = P2nPlus1(testX, x, y, z)
print(myY)

plt.plot(testX, trueY, color="red", label="Ground Truth")
plt.plot(testX, myY, color="blue", label="Approximation")

plt.legend()
plt.show()

