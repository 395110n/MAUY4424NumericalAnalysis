import math

# f(x) = sin(x)
import math

def f(x):
    return math.sin(x)

def df(x):
    return math.cos(x)

def secant_method_update(xk, xk_, df):
    return xk - df(xk) * (xk - xk_) / (df(xk) - df(xk_))

def mini():
    tol = 10 ** (-8)
    roots = []
    prevx = -10 
    for num in range(-9, 10):
        x_hat = num  # Save current value of x_hat
        while x_hat >= -10 and x_hat <= 10:
            x_hat_ = secant_method_update(x_hat, prevx, df)
            if abs(df(x_hat_)) > tol:
                prevx = x_hat
                x_hat = x_hat_
            else:
                if (df(x_hat + 0.5) >= 0 and df(x_hat - 0.5) <= 0):
                    roots.append(x_hat)
                    minim = f(x_hat)
                break
        prevx = num
    return roots, minim

print(mini())
