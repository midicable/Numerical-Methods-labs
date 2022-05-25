from math import exp

def func(arg):
    return exp(-arg) - (arg - 1)**2
def funcFirstDerivative(arg):
    return -exp(-arg) - 2 * (arg - 1)
def funcSecondDerivative(arg):
    return exp(-arg) - 2

def dichotomyMethod(left_boundary, right_boundary, eps):
    midpoint = 0.
    iterations = 0
    while right_boundary - left_boundary > 2 * eps:
        iterations += 1
        midpoint = (left_boundary + right_boundary) / 2
        if func(left_boundary) * func(midpoint) < 0:
            right_boundary = midpoint
        else:
            left_boundary = midpoint
    return midpoint, iterations

def simpleIteration(x0, eps):
    x_prev = x0
    x_curr = exp(-x0 / 2) + 1
    iterations = 1
    while abs(x_curr - x_prev) > eps:
        iterations += 1
        x_prev = x_curr
        x_curr = exp(-x_prev / 2) + 1
    return x_curr, iterations

def newtonMethod(x0, eps):
    x_prev = x0
    x_curr = x0 - func(x0) / funcFirstDerivative(x0)
    iterations = 1
    while abs(x_curr - x_prev) > eps:
        iterations += 1
        x_prev = x_curr
        x_curr = x_prev - func(x_prev) / funcFirstDerivative(x_prev)
    return x_curr, iterations

def chebyshevMethod(x0, eps):
    x_prev = x0
    x_curr = x0 - func(x0) / funcFirstDerivative(x0) - \
             ( pow(func(x0), 2) * funcSecondDerivative(x0) ) / ( 2 * pow(funcFirstDerivative(x0), 3) )
    iterations = 1
    while abs(x_curr - x_prev) > eps:
        iterations += 1
        x_prev = x_curr
        x_curr = x_prev - func(x_prev) / funcFirstDerivative(x_prev) - \
                 ( pow(func(x_prev), 2) * funcSecondDerivative(x_prev) ) / ( 2 * pow(funcFirstDerivative(x_prev), 3) )
    return x_curr, iterations

