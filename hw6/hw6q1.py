import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return np.exp(np.power(x, 3)) + np.sin(np.power(x, 2)) + x

def func2(x):
    return np.cos(np.power(x, 5) + 4 * np.power(x, 4) + 3 * np.power(x, 3) + 2 * np.power(x, 2) + x + 1)

def compositeTrapzoid(func, start, end, steps):
    trapzoid = np.zeros(9)
    for ind in range(steps.shape[0]):
        x = np.arange(start, end+steps[ind], steps[ind])
        trapzoid[ind] = steps[ind] * (func(x[0]) / 2 + func(x[-1]) / 2 + np.sum(func(x[1:-1])))
    return trapzoid

def compositeSimpsons(func, start, end, steps):
    simpsons = np.zeros(9)
    for ind in range(steps.shape[0]):
        x = np.arange(start, end+steps[ind], steps[ind])
        simpsons[ind] = steps[ind] * \
        (func(x[0]) + func(x[-1]) + \
         4* np.sum(func(x[1:-1:2])) + 2 * np.sum(func(x[2:-1:2])) \
         ) / 3
    return simpsons

pw = np.arange(0, 9)
steps = 0.5 ** pw

func1Trapzoid = compositeTrapzoid(func1, -1, 1, steps)
func1Simpsons = compositeSimpsons(func1, -1, 1, steps)

plt.plot(steps, func1Trapzoid, color="red", label="func1Trapzoid")
plt.plot(steps, func1Simpsons, color="blue", label="func1Simpsons")
plt.legend()
plt.xscale("log", base=2)
plt.savefig("hw6q1a.png")
plt.show()

func2Trapzoid = compositeTrapzoid(func2, 0, 2, steps)
func2Simpsons = compositeSimpsons(func2, 0, 2, steps)

plt.plot(steps, func2Trapzoid, color="red", label="func2Trapzoid")
plt.plot(steps, func2Simpsons, color="blue", label="func2Simpsons")
plt.legend()
plt.xscale("log", base=2)
plt.savefig("hw6q1b.png")
plt.show()
