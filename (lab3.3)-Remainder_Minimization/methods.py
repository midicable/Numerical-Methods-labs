from math import exp, sin, cos, pi, factorial


n = 10
a = 0.3
b = 1.3
M = 1.288038180323


def f(arg):
    return 0.3 * exp(arg) + 0.7 * sin(arg)


def chebyshevNodes():
    nodes = list()
    for k in range(n + 1):
        nodes.append(0.5 * (b + a) + 0.5 * (b - a) * cos(((2 * k + 1) * pi) / (2 * (n + 1))))
    return nodes


def functionOf(X):
    Y = [f(X[i]) for i in range(n + 1)]
    return Y


def lagrangeInterpolation(X, Y, arg):
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


def interpolationRemainder():
    return (M * (b - a)**(n + 1)) / (factorial(n + 1) * 2**(2 * n + 1))


