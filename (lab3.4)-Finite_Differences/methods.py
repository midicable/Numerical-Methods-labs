from math import sin, exp


def f(arg):
    return 0.3 * exp(arg) + 0.7 * sin(arg)


def finiteDifferencesInterpolation(arg, x0, h, deltas):
    t = (arg - x0) / h
    return deltas[0] + t * deltas[1] + (t * (t - 1)) / 2 * deltas[2] \
                            + (t * (t - 1) * (t - 2)) / 6 * deltas[3]


def interpolationRemainder(arg, x0, h):
    t = (arg - x0) / h
    return abs((h**4) * t * (t - 1) * (t - 2) * (t - 3) / 24 * f(0.45))
