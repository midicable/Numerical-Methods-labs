import copy

from functions.evaluator import k, k_first_derivative, q, f
from coefficients.evaluator import get_kappa0_wave, get_kappa1_wave, get_g0_wave, get_g1_wave
from additional.constants import KAPPA_0, KAPPA_1, G_0, G_1


def form_matrix_1(N):
    h = 1 / N                         # шаг сетки
    x = [i * h for i in range(N + 1)] # равномерная сетка

    A = [.0] * (N + 1)  # коэффиценты при y_i-1
    B = [.0] * (N + 1)  # коэффиценты при y_i
    C = [.0] * (N + 1)  # коэффиценты при y_i+1
    F = [.0] * (N + 1)  # правый столбец системы

    B[0] =  k(x[0]) / h + get_kappa0_wave(KAPPA_0, h) # нашли B[0]
    C[0] = -k(x[0]) / h                               # нашли C[0]
    F[0] = get_g0_wave(G_0, h)                        # нашли F[0]

    for i in range(1, N):                             # в цикле вычисляем A_i, B_i ,C_i, F_i
        A[i] = -k_first_derivative(x[i]) / (2 * h) + k(x[i]) / h**2
        B[i] = ( -2 * k(x[i]) ) / h**2 - q(x[i])
        C[i] = ( k_first_derivative(x[i]) / (2 * h) ) + ( k(x[i]) / h**2 )
        F[i] = -f(x[i])

    A[N] = k(x[N]) / h                                    # нашли A[N]
    B[N] = -( k(x[N]) / h + get_kappa1_wave(KAPPA_1, h) ) # нашли B[N]
    F[N] = -get_g1_wave(G_1, h)                           # нашли F[N]

    return A, B, C, F


def form_matrix_2(N):
    h = 1 / N                         # шаг сетки
    x = [i * h for i in range(N + 1)] # равномерная сетка

    A = [.0] * (N + 1)  # коэффиценты при y_i-1
    B = [.0] * (N + 1)  # коэффиценты при y_i
    C = [.0] * (N + 1)  # коэффиценты при y_i+1
    F = [.0] * (N + 1)  # правый столбец системы

    B[0] = - ( KAPPA_0 + k(x[0] + 0.5 * h) / h + 0.5 * h * q(x[0]) ) # нашли B[0]
    C[0] = k(x[0] + 0.5 * h) / h                                     # нашли C[0]
    F[0] = - ( 0.5 * h * f(x[0]) + G_0 )                             # нашли F[0]

    for i in range(1, N):                             # в цикле вычисляем A_i, B_i ,C_i, F_i
        A[i] = k(x[i] - 0.5 * h) / h
        B[i] = - ( k(x[i] + 0.5 * h) / h + k(x[i] - 0.5 * h) / h + h * q(x[i]) )
        C[i] = k(x[i] + 0.5 * h) / h
        F[i] = - h * f(x[i])

    A[N] = k(x[N] - 0.5 * h) / h                                      # нашли A[N]
    B[N] = - ( KAPPA_1 + k(x[N] - 0.5 * h) / h  + 0.5 * h * q(x[N]) ) # нашли B[N]
    F[N] = - ( 0.5 * h * f(x[N]) + G_1 )                              # нашли F[N]

    return A, B, C, F


def form_matrix_3(N):
    h = 1 / N                         # шаг сетки
    x = [i * h for i in range(N + 1)] # равномерная сетка

    A = [.0] * (N + 1)  # коэффиценты при y_i-1
    B = [.0] * (N + 1)  # коэффиценты при y_i
    C = [.0] * (N + 1)  # коэффиценты при y_i+1
    F = [.0] * (N + 1)  # правый столбец системы

    B[0] = ( k(x[0]) + k(x[1]) ) / (2 * h) + 0.5 * h * q(x[0]) + KAPPA_0     # нашли B[0]
    C[0] = - ( ( k(x[0]) + k(x[1]) ) / (2 * h) )                             # нашли C[0]
    F[0] = 0.5 * h * f(x[0]) + G_0                                           # нашли F[0]

    for i in range(1, N):                             # в цикле вычисляем A_i, B_i ,C_i, F_i
        A[i] = ( k(x[i - 1]) + k(x[i]) ) / (2 * h**2)
        B[i] = - ( ( k(x[i - 1]) + 2 * k(x[i]) + k(x[i + 1]) + 2 * q(x[i]) * h**2 ) / (2 * h**2) )
        C[i] =  ( k(x[i]) + k(x[i + 1]) ) / (2 * h**2)
        F[i] = - f(x[i])

    A[N] = - ( ( k(x[N - 1]) + k(x[N]) ) / (2 * h) )                            # нашли A[N]
    B[N] = ( k(x[N - 1]) + k(x[N]) ) / (2 * h) + 0.5 * h * q(x[N]) + KAPPA_1    # нашли B[N]
    F[N] = 0.5 * h * f(x[N]) + G_1                                              # нашли F[N]

    return A, B, C, F