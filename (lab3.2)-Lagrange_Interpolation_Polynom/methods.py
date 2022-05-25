from math import factorial, exp, sin

n = 10
m = 5


def f(arg):
    return 0.3 * exp(arg) + 0.7 * sin(arg)


def sampling(x0, sample_rate):
    X = [x0 + sample_rate * i for i in range(n + 1)]
    Y = [anthonyF(X[i]) for i in range(n + 1)]

    return X, Y


def lagrangeInterpolation(arg, X, Y):
    totalSum    = 0
    totalProd   = 1
    for k in range(len(X)):
        totalProd = 1
        for j in range(len(X)):
            if j != k:
                totalProd *= (arg - X[j]) / (X[k] - X[j])
        totalProd *= Y[k]
        totalSum += totalProd
    return totalSum


def interpolationRemainder(arg, X):
    maximum     = 1.288038180323
    omega       = 1
    remainder   = 1
    for i in range(len(X)):
        omega *= (arg - X[i])
    remainder = (omega * maximum) / factorial(len(X))
    return remainder