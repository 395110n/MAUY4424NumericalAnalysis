import math

def f(x):
    if x != 0:
        return math.sin(x) / x
    else:
        return 1
    
def df(x):
    if x != 0:
        return (math.cos(x) / x) - (math.sin(x) / (x**2))
    else:
        return 0
    


def newton():
    roots = []
    tol = 10 ** (-7)
    for num in range(-10, 11):
        x_hat = num
        counter = 0 
        while x_hat <= 10 and x_hat >= -10:
            fx = f(x_hat)
            dfx = df(x_hat)
            if (abs(dfx) < tol):
                if fx != 0:
                    print(f"drop guess: {x_hat}")
                    break # if f'(x) == 0 and f(x) != 0, then initial guess x_hat is not a good guess, so we discard this inital guess and pass to the next
            if abs(f(x_hat)) < tol:
                if x_hat not in roots and x_hat + tol not in roots and x_hat - tol not in roots:
                    roots.append(x_hat)
                    print(f"found used {counter} rounds, x_hat = {x_hat}")
                break
            else:
                x_hat -= fx / dfx
                x_hat = round(x_hat, 7)
            counter += 1
            
    return roots

print(newton())