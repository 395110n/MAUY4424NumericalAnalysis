import math

# f(x) = -sin(x) / x

def f(x):
    return -math.sin(x) / x

def df(x):
    return -(x * math.cos(x) - math.sin(x)) / x ** 2

def secant_method_update(xk, xk_, df):
    return xk - df(xk)*(xk - xk_) / (df(xk) - df(xk_))

def mini():
    tol = 10 ** (-8)
    prevx = -10
    roots = []
    min = []
    for num in range(-9, 11):
        x_hat = num
        while abs(x_hat) >= -10 and abs(x_hat) <= 10:
            if (x_hat == 0) or (prevx == 0): break

            if abs(df(x_hat)) < tol:
                if df(x_hat - 0.5) < 0 and df(x_hat + 0.5) > 0:
                    roots.append(x_hat)
                    min.append(f(x_hat))
                break
            else:
                x_hat_ = secant_method_update(x_hat, prevx, df)
                if abs(x_hat_) > 0 and abs(x_hat_) < tol: break
                prevx, x_hat = x_hat, x_hat_
                print("iteration", num , "prevx = ", prevx, "x_hat_ = ", x_hat_)
                
        prevx = num
    return roots, min

print(mini())

