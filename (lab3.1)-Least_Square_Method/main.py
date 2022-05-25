from methods import sampling, leastSquareMethod

x0 = 0.3
h  = 0.1

X, Y = sampling(x0, h)
C = leastSquareMethod(X, Y)

for i in range(4):
    print(f'C[{i}] = {C[i]}')
print()

