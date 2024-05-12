abs(df(x_hat)) <= tol and abs(df(x_hat)) > 0:
                if (f(x_hat) <= minim):
                    roots.append(x_hat)
                    minim = f(x_hat)