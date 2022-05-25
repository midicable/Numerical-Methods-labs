from math import exp, sin, sqrt
import numpy as np

n = 10
m = 5

def f(arg):
    return 0.3 * exp(arg) + 0.7 * sin(arg)


def phi(C, arg):
    total = 0
    for i in range(m + 1):
        total += C[i] * arg**i
    return total


def sampling(x0, sample_rate):
    X = [x0 + sample_rate * i for i in range(n + 1)]
    Y = [f(X[i]) for i in range(n + 1)]
    
    return X, Y

def leastSquareMethod(X, Y):
    A = [[0] * (m + 1) for _ in range(m + 1)] 
    b = [0] * (m + 1)                         

    for l in range(m + 1):
        for k in range(m + 1):
            sum = 0
            for i in range(n + 1):
                sum += X[i]**(k + l)
            A[l][k] = sum
        sum = 0
        for i in range(n + 1):
            sum += Y[i] * X[i]**l
        b[l] = sum

    C = np.linalg.inv(np.array(A)).dot(np.array(b))

    return C









