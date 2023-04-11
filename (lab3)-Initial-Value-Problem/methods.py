from math import log


def func(t, u):
    return (u**2 * log(t) - u) / t

def backward_euler(a, b, N):
    eps = 0.001
    h = (b - a) / N
    t = [a + i * h for i in range(N + 1)]
    u = [1] + [0 for i in range(N)]
    for i in range(N):
        u_prev = u[i]
        u_curr = u_prev - (h * log(t[i + 1]) * u_prev**2 - (h + t[i + 1]) * u_prev + u[i] * t[i + 1]) / \
                     (2 * h * log(t[i + 1]) * u_prev - (h + t[i + 1]))
        while (abs(u_curr - u_prev) > eps):
            u_prev = u_curr
            u_curr = u_prev - (h * log(t[i + 1]) * u_prev**2 - (h + t[i + 1]) * u_prev + u[i] * t[i + 1]) / \
                     (2 * h * log(t[i + 1]) * u_prev - (h + t[i + 1]))
        u[i + 1] = u_curr
    print(*u, sep='\n')
    return u


def runge_kutta(a, b, N):
    h = (b - a) / N
    t = [a + i * h for i in range(N + 1)]
    u = [1] + [0 for i in range(N)]
    for i in range(N):
        k1 = func(t[i], u[i])
        k2 = func(t[i + 1], u[i] + h * k1)
        u[i + 1] = u[i] + 0.5 * h * (k1 + k2)
    print(*u, sep='\n')
    return u

def successive_order_boosting_second_order(a, b, N):
    h = (b - a) / N
    t = [a + i * h for i in range(N + 1)]
    u = [1] + [0 for i in range(N)]
    for i in range(N):
        u_half_i = u[i] + 0.5 * h * func(t[i], u[i])
        u[i + 1] = u[i] + h * func(t[i] + 0.5 * h, u_half_i)
    print(*u, sep='\n')
    return u

def successive_order_boosting_third_order(a, b, N):
    h = (b - a) / N
    t = [a + i * h for i in range(N + 1)]
    u = [1] + [0 for i in range(N)]
    for i in range(2):
        u_one_third = u[i] + (1 / 3) * h * func(t[i], u[i])
        u_two_third = u[i] + (2 / 3) * h * func(t[i] + (1 / 3) * h, u_one_third)
        u[i + 1] = u[i] + (1 / 4) * h * (func(t[i], u[i]) + 3 * func(t[i] + (2 / 3) * h, u_two_third))
    return u


def extrapolation_adams_method(a, b, N):
    h = (b - a) / N
    t = [a + i * h for i in range(N + 1)]
    u = successive_order_boosting_third_order(a, b, N)
    for i in range(3, N + 1):
        u[i] = u[i - 1] + (1 / 12) * h * (23 * func(t[i - 1], u[i - 1]) -
                                          (48 / 3) * func(t[i - 2], u[i - 2]) +
                                          5 * func(t[i - 3], u[i - 3]))
    print(*u, sep='\n')
    return u



