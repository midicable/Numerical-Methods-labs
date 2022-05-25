from methods import*

h = 0.1

nodes = [0 + (2/3) * h, 0.5 + (1/2) * h, 2 - (1/3) * h]

X = chebyshevNodes()
Y = functionOf(X)

print('X:', end=' ')
for i in range(n + 1):
    print(X[i], end=' ')
print()
print('Y:', end=' ')
for i in range(n + 1):
    print(Y[i], end=' ')
print()

print()

for i in range(3):
    print(f'P({i + 1}) = {lagrangeInterpolation(X, Y, nodes[i])}')

print()

for i in range(3):
    print(f'e({i + 1}) = {abs(f(nodes[i]) - lagrangeInterpolation(X, Y, nodes[i]))}')

print()

print(f'r = {interpolationRemainder()}')