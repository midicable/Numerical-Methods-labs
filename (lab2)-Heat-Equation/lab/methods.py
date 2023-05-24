from functions.evaluator import f, phi, mu_1, mu_2
from linalg.methods import tridiagonal_method


def solve_heat_equation(h, t):
    N1 = int(1 / h) # количество разбиений по h
    N2 = int(1 / t) # количество разбиений по t
    u = []          # массив для решения

    u.append([phi(j * h) for j in range(N1 + 1)]) # заполняем 1-ый слой
    for i in range(N2):
        A = [0] * (N1 + 1)
        B = [0] * (N1 + 1)
        C = [0] * (N1 + 1)
        F = [0] * (N1 + 1)

        # формируем матрицу системы для нахлжденея следующего слоя
        B[0] = 1
        C[0] = 0
        F[0] = mu_1(i * t)

        for j in range(1, N1):
            A[j] = -t / (4 * h**2)
            B[j] = 1 + t / (2 * h**2)
            C[j] = -t / (4 * h**2)
            F[j] = u[i][j] + (3 * t / 4 * h**2) * (u[i][j - 1] - 2 * u[i][j] + u[i][j + 1]) + t * f(j * h, i * t)

        A[N1] = -1
        B[N1] = 1 + h**2 / (2 * t)
        F[N1] = h * mu_2(i * t) + (h**2 / (2 * t)) * u[i][N1] + (h**2 / 2) * f(N1 * h, i * t)

        u.append(tridiagonal_method(A, B, C, F, N1))

    return u




