from math import exp


def f(x, t):
    return -(x + t**2) * exp(-x * t)

def phi(x):
    return 1

def mu_1(t):
    return 1

def mu_2(t):
    return t * exp(-t)