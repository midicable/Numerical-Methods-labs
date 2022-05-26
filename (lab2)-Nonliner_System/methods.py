from math import sin, cos
import numpy as np
#--------------------------------------
def func1(x, y):
    return (x - 1)**2 + y**2 - 4
def func1FirstDerivative(x, y):
    return 2 * (x - 1)
def func2(x, y):
    return 2 * y - sin(x - 1)
def func2FirstDerivative(x, y):
    return 2
def func1XPartialDerivative(x, y):
    return 2 * (x - 1)
def func1YPartialDerivative(x, y):
    return 2 * y
def func2XPartialDerivative(x, y):
    return -0.5 * cos(x - 1)
def func2YPartialDerivative(x, y):
    return 1

def GaussSeidelMethod(x0, y0, eps):
    iterations = 1

    x_prev_GaussSeidel, y_prev_GaussSeidel = x0, y0
    x_prev_Newton, y_prev_Newton = x_prev_GaussSeidel, y_prev_GaussSeidel

    #процесс нахождения x(1)
    x_curr_Newton = x_prev_Newton - func1(x_prev_Newton, y_prev_GaussSeidel) /\
                                    func1FirstDerivative(x_prev_Newton, y_prev_GaussSeidel)
    while abs(x_curr_Newton - x_prev_Newton) > eps:
        x_prev_Newton = x_curr_Newton
        x_curr_Newton = x_prev_Newton - func1(x_prev_Newton, y_prev_GaussSeidel) /\
                                 func1FirstDerivative(x_prev_Newton, y_prev_GaussSeidel)
    x_curr_GaussSeidel = x_curr_Newton

    # процесс нахождения y(1)
    y_curr_Newton = y_prev_Newton - func2(x_curr_GaussSeidel, y_prev_Newton) /\
                                    func1FirstDerivative(x_curr_GaussSeidel, y_prev_GaussSeidel)
    while abs(y_curr_Newton - y_prev_Newton) > eps:
        y_prev_Newton = y_curr_Newton
        y_curr_Newton = y_prev_Newton - func2(x_curr_GaussSeidel, y_prev_Newton) /\
                                 func2FirstDerivative(x_curr_GaussSeidel, y_prev_Newton)
    y_curr_GaussSeidel = y_curr_Newton

    while max(abs(x_curr_GaussSeidel - x_prev_GaussSeidel), abs(y_curr_GaussSeidel - y_prev_GaussSeidel)) > eps:
        iterations += 1

        x_prev_GaussSeidel = x_curr_GaussSeidel
        y_prev_GaussSeidel = y_curr_GaussSeidel

        x_prev_Newton = x_prev_GaussSeidel
        x_curr_Newton = x_prev_Newton - func1(x_prev_Newton, y_prev_GaussSeidel) / \
                        func1FirstDerivative(x_prev_Newton, y_prev_GaussSeidel)

        while abs(x_curr_Newton - x_prev_Newton) > eps:
            x_prev_Newton = x_curr_Newton
            x_curr_Newton = x_prev_Newton - func1(x_prev_Newton, y_prev_GaussSeidel) / \
                            func1FirstDerivative(x_prev_Newton, y_prev_GaussSeidel)
        x_curr_GaussSeidel = x_curr_Newton

        y_prev_Newton = y_prev_GaussSeidel
        y_curr_Newton = y_prev_Newton - func2(x_curr_GaussSeidel, y_prev_Newton) / \
                        func1FirstDerivative(x_curr_GaussSeidel, y_prev_GaussSeidel)
        while abs(y_curr_Newton - y_prev_Newton) > eps:
            y_prev_Newton = y_curr_Newton
            y_curr_Newton = y_prev_Newton - func2(x_curr_GaussSeidel, y_prev_Newton) / \
                     func2FirstDerivative(x_curr_GaussSeidel, y_prev_Newton)
        y_curr_GaussSeidel = y_curr_Newton

    return x_curr_GaussSeidel, y_curr_GaussSeidel, iterations
#---------------------------------------


def SecantMethod(x0, y0, eps):
    v0 = np.array([[x0], [y0]])
    J = [[func1XPartialDerivative(x0, y0), func1YPartialDerivative(x0, y0)],
         [func2XPartialDerivative(x0, y0), func2YPartialDerivative(x0, y0)]]

    delta = np.linalg.solve(J, [[(-1) * func1(v0[0][0], v0[1][0])], [(-1) * func2(v0[0][0], v0[1][0])]])
    v1 = v0 + delta

    iterations = 1
    while np.linalg.norm(v1 - v0, ord=np.inf) > eps:
        J = [[(func1(v1[0][0], v1[1][0]) - func1(v0[0][0], v1[1][0])) / (v1[0][0] - v0[0][0]),
              (func1(v1[0][0], v1[1][0]) - func1(v1[0][0], v0[1][0])) / (v1[1][0] - v0[1][0])],
             [(func2(v1[0][0], v1[1][0]) - func2(v0[0][0], v1[1][0])) / (v1[0][0] - v0[0][0]),
              (func2(v1[0][0], v1[1][0]) - func2(v1[0][0], v0[1][0])) / (v1[1][0] - v0[1][0])]]

        delta = np.linalg.solve(J, [[(-1) * func1(v1[0][0], v1[1][0])], [(-1) * func2(v1[0][0], v1[1][0])]])
        v2 = v1 + delta
        v0 = v1
        v1 = v2
        iterations += 1

    x_curr_secant = v1[0][0]
    y_curr_secant = v1[1][0]

    return x_curr_secant, y_curr_secant, iterations