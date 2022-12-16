from numpy import linalg as la


# для реализации обоих методов используется
# составная формула левых прямоугольнков
# поэтому в качестве сетки на отрезке [0; 1]
# берем множество {0.0, 0.2, ..., 0.9} - 10 узлов

def kernel(x, s):
    return 1 / (1 + x + s)

def func(x):
    return 1 + x

def volterra_mechanical_quadrature(a, b, N, lambda_):
    h = (b - a) / N
    x = [a + i * h for i in range(N)]
    A = [[0 for j in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(i + 1):
            if i == j:
                A[i][j] = 1 - lambda_ * h * kernel(x[i], x[j])
            else:
                A[i][j] = -lambda_ * h * kernel(x[i], x[j])
    f = [func(x[i]) for i in range(N)]
    u = list(la.solve(A, f))

    x_ = (a + b) / 2.2
    quadrature_sum = 0
    for k in range(N):
        quadrature_sum += kernel(x_, x[k]) * u[k]
    u_ = lambda_ * h * quadrature_sum + func(x_)

    return u, u_

def volterra_successive_aproximations(a, b, N, lambda_, n):
    h = (b - a) / N
    x = [a + i * h for i in range(N)]
    y_prev = [0 for i in range(N)]          # начальное приближение, в предположении, что y(x) = 0
    y_curr = [0 for i in range(N)]          # следующее приближение
    for iteration in range(n):
        for i in range(N):
            quadrature_sum = 0
            for k in range(i):
                quadrature_sum += kernel(x[i], x[k]) * y_prev[k]
            y_curr[i] = lambda_ * h * quadrature_sum + func(x[i])
        y_prev = y_curr.copy()
    u = y_curr

    x_ = (a + b) / 2.2
    quadrature_sum = 0
    for k in range(N):
        quadrature_sum += kernel(x_, x[k]) * u[k]
    u_ = lambda_ * h * quadrature_sum + func(x_)

    return u, u_
