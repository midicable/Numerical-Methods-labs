from math import sqrt, asin


def f(x):
    return asin(sqrt(x)) / sqrt(x * (1 - x))


def F(x):
    a, b = 0.2, 0.3
    return 0.5 * (b - a) * (asin(sqrt(0.5 * (b - a) * x + 0.5 * (b + a))) /
                             sqrt((0.5 * (b - a) * x + 0.5 * (b + a)) * (1 - 0.5 * (b - a) * x - 0.5 * (b + a))))


def runge_rule(a, b, eps):
    h1, h2 = b - a, (b - a) / 2
    N1, N2 = 1, 2
    Q1 = left_rectangles_formula(a, h1, N1)
    Q2 = left_rectangles_formula(a, h2, N2)
    R = (Q1 - Q2) / (1 - (h2/h1))
    i = 1
    while abs(R) > eps:
        i += 1
        h1 = h2
        h2 = h1 / 2
        N2 = 2**i
        Q1 = Q2
        Q2 = left_rectangles_formula(a, h2, N2)
        R = (Q1 - Q2) / (1 - (h2/h1))

    return round(Q2, 11), round(h2, 6)


def left_rectangles_formula(a, h, N):
    Q = 0
    for k in range(N):
        Q += f(a + k * h)
    Q *= h
    return Q


def middle_rectangles_formula(a, h, N):
    Q = 0
    for k in range(N):
        Q += f(a + (k + 0.5) * h)
    Q *= h
    return round(Q, 11)

def simpsons_formula(a, h, N):
    Q = 0
    for k in range(N):
        Q += (f(a + k * h) + 4 * f(a + (k + 0.5) * h) + f(a + (k + 1) * h))
    Q *= (h / 6)
    return round(Q, 11)


def gauss_quadrature_formula():
    x1, x2, x3 = -sqrt(0.6), 0, sqrt(0.6)
    return round((5/9) * F(x1) + (8/9) * F(x2) + (5/9) * F(x3), 11)

def gauss_quadrature_remainder():
    return (49.2474 * 16) * 0.1**5 / (24**3 * 5)