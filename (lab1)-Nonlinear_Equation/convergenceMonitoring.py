from math import exp, log10
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def func(arg):
    return exp(-arg) - (arg - 1)**2
def funcFirstDerivative(arg):
    return -exp(-arg) - 2 * (arg - 1)
def funcSecondDerivative(arg):
    return exp(-arg) - 2

fig, ax = plt.subplots()
plt.title('График сходимости итерационных методов')
ax.grid(color='black', linewidth=0.8, linestyle='--')
plt.xlim([-14, 0])
plt.ylim([-14, 0])
plt.xlabel('lg(|x(n - 1) - X*|)')
plt.ylabel('lg(|x(n) - X*|)')
plt.grid(True)

def MSIConvergence(x0, eps, root):
    X, Y = [], []
    x_prev = x0
    x_curr = exp(-x0 / 2) + 1
    X.append(log10(abs(x_prev - root)))
    Y.append(log10(abs(x_curr - root)))
    while abs(x_curr - x_prev) > eps:
        x_prev = x_curr
        x_curr = exp(-x_prev / 2) + 1
        X.append(log10(abs(x_prev - root)))
        Y.append(log10(abs(x_curr - root)))
    x = np.array([-0.2820550815317945, -0.9594347580832739, -1.5693618359347605, -2.1941871157816952,
                  -2.815394619435938, -3.437462666322879, -4.05932498665886, -4.681236430824803,
                  -5.303136139886219, -5.925038659910685, -6.546940473984423, -7.168842600776156], dtype=object).reshape((-1, 1))
    y = np.array([-0.9594347580832739, -1.5693618359347605, -2.1941871157816952, -2.815394619435938,
                  -3.437462666322879, -4.05932498665886, -4.681236430824803, -5.303136139886219,
                  -5.925038659910685, -6.546940473984423, -7.168842600776156, -7.7907440498962375], dtype=object)
    model = LinearRegression()
    model.fit(x, y)
    print('MSI interception:', model.intercept_)
    plt.plot(X, Y, 'o-b', alpha=0.5, label="Метод простых итерций", lw=2.5, ms=3.5)
    plt.plot([-14, -0.282], [-14 * model.coef_, -0.282 * model.coef_ + model.intercept_], label='y = 0.99704569x - 0.63679',marker='.', ls='-', ms=0.5, color='c', alpha=1, lw=0.8)

def NewtonConvergence(x0, eps, root):
    X, Y = [], []
    x_prev = x0
    x_curr = x0 - func(x0) / funcFirstDerivative(x0)
    X.append(log10(abs(x_prev - root)))
    Y.append(log10(abs(x_curr - root)))
    while abs(x_curr - x_prev) > eps:
        x_prev = x_curr
        x_curr = x_prev - func(x_prev) / funcFirstDerivative(x_prev)
        X.append(log10(abs(x_prev - root)))
        Y.append(log10(abs(x_curr - root)))
    x = np.array([-0.2820550815317945, -0.9303380245516413, -2.053074373830556, -4.237318454588522], dtype=object).reshape((-1, 1))
    y = np.array([-0.9303380245516413, -2.053074373830556, -4.237318454588522, -8.600448817824242], dtype=object)
    model = LinearRegression()
    model.fit(x, y)
    print('Newton interception:', model.intercept_)
    plt.plot(X, Y, 'o-g', alpha=0.5, label="Метод Ньютона", lw=2.5, ms=3.5)
    plt.plot([-9, -0.282], [-9 * model.coef_, -0.282 * model.coef_ + model.intercept_], label='y = 1.95077099x - 0.29624', marker='.', ls='-', ms=0.5, color='m', alpha=1, lw=0.8)

def ChebyshevConvergence(x0, eps, root):
    X, Y = [], []
    x_prev = x0
    x_curr = x0 - func(x0) / funcFirstDerivative(x0) - \
             (pow(func(x0), 2) * funcSecondDerivative(x0)) / (2 * pow(funcFirstDerivative(x0), 3))
    X.append(log10(abs(x_prev - root)))
    Y.append(log10(abs(x_curr - root)))
    while abs(x_curr - x_prev) > eps:
        x_prev = x_curr
        x_curr = x_prev - func(x_prev) / funcFirstDerivative(x_prev) - \
                 (pow(func(x_prev), 2) * funcSecondDerivative(x_prev)) / (2 * pow(funcFirstDerivative(x_prev), 3))
        X.append(log10(abs(x_prev - root)))
        Y.append(log10(abs(x_curr - root)))
    x = np.array([-0.2820550815317945, -1.3390798426536337, -4.041560226025774], dtype=object).reshape((-1, 1))
    y = np.array([-1.3390798426536337, -4.041560226025774, -12.079760192311282], dtype=object)
    model = LinearRegression()
    model.fit(x, y)
    print('Chebyshev:', model.intercept_)
    plt.plot(X, Y, 'o-y', alpha=0.5, label="Метод Чебышева", lw=2.5, ms=3.5)
    plt.plot([-7, -0.282], [model.coef_*-7, -0.282 * model.coef_ + + model.intercept_], label='y = 2.88009389x - 0.38377', marker='.', ls='-', ms=0.5, color='r', alpha=1, lw=0.8)
    plt.legend()
    plt.show()

