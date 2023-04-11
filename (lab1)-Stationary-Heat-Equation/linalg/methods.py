def tridiagonal_method(A, B, C, F, N):
    alpha = [.0] * N
    beta  = [.0] * N

    # этап прямой прогонки (вычисление прогоночных коэффициентов)
    alpha[0] = -C[0] / B[0]
    beta[0]  =  F[0] / B[0]
    for i in range(1, N):
        alpha[i] = -C[i] / (B[i] + A[i] * alpha[i - 1])
        beta[i]  = (F[i] - A[i] * beta[i - 1]) / (B[i] + A[i] * alpha[i - 1])

    y = [.0] * (N + 1)
    # этап обратной прогонки (вычисление неизвестных)
    y[N] = (F[N] - A[N] * beta[N - 1]) / (B[N] + A[N] * alpha[N - 1])
    for i in range(N - 1, -1, -1):
        y[i] = alpha[i] * y[i + 1] + beta[i]

    return y
