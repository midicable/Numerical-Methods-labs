from functions.evaluator import k, k_first_derivative, q, f


def get_kappa0_wave(KAPPA_0, h):
    return KAPPA_0 * (1 - (h * k_first_derivative(0)) / (2 * k(0))) + 0.5 * h * q(0)


def get_g0_wave(G_0, h):
    return G_0 * (1 - (h * k_first_derivative(0)) / (2 * k(0))) + 0.5 * h * f(0)


def get_kappa1_wave(KAPPA_1, h):
    return KAPPA_1 * (1 + (h * k_first_derivative(1)) / (2 * k(1))) + 0.5 * h * q(1)


def get_g1_wave(G_1, h):
    return G_1 * (1 + (h * k_first_derivative(1)) / (2 * k(1))) + 0.5 * h * f(1)