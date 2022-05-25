from methods import*

x0 = 0.3
h  = 0.1
x  = x0 + (2/3) * h

X = [0.3, 0.4, 0.5, 0.6]
Y = [f(X[i]) for i in range(4)]

delta1Y = [f(X[i + 1]) - f(X[i]) for i in range(3)]
delta2Y = [delta1Y[i + 1] - delta1Y[i] for i in range(2)]
delta3Y = [delta2Y[i + 1] - delta2Y[i] for i in range(1)]

deltas = [0.6118217869357386, 0.10831846197269779, 0.0017555473518463538, -0.0001584434156937098]

P = finiteDifferencesInterpolation(x, x0, h, deltas)
R = interpolationRemainder(x, x0, h)
r = f(x) - P

print(f'f(x*) = {f(x)}')
print(f'P(x*) = {P}')
print(f'R(x*) = {R}')
print(f'r(x*) = {r}')




