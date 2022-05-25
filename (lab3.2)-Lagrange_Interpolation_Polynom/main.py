from methods import*

x0 = 0.15
h  = 0.1

X, Y = sampling(x0, h)

nodes = list()
nodes.append(X[0] + (2/3) * h)
nodes.append(X[5] + (1/2) * h)
nodes.append(X[10] - (1/3) * h)

for i in range(3):
    print(f'P(x({i + 1})) = {lagrangeInterpolation(nodes[i], X, Y)}')
print()
for i in range(3):
    print(f'e(x{i + 1}) = {abs(lagrangeInterpolation(nodes[i], X, Y) - anthonyF(nodes[i]))}')
print()
for i in range(3):
    print(f'r(x{i + 1}) = {interpolationRemainder(nodes[i], X)}')