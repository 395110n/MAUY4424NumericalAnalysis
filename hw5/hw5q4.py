import numpy as np
import matplotlib.pyplot as plt

def trapzium(a, b, func):
    return (b - a) * (func(a) + func(b)) / 2

def simpsons(a, b, func):
    return (b - a) * (func(a) + 4 * func((a+b)/2) + func(b)) / 6

def func1(x):
    return np.exp(np.power(x, 3)) + np.sin(np.power(x, 2)) + x

def func2(x):
    return np.cos(np.power(x, 5) + 4 * np.power(x, 4) + 3 * np.power(x, 3) + 2*np.power(x, 2) + x + 1)

h = np.array([1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625])

func1_trap = trapzium(-h, h, func1)
func1_simp = simpsons(-h, h, func1)

plt.plot(h, func1_trap, color="red", label="Trapzium Func1")
plt.plot(h, func1_simp, color="blue", label="Simpsons Func1")
plt.legend()
plt.show()

func2_trap = trapzium(0, h, func2)
func2_simp = simpsons(0, h, func2)

plt.plot(h, func2_trap, color="red", label="Trapzium Func2")
plt.plot(h, func2_simp, color="blue", label="Simpsons Func2")
plt.legend()
plt.show()