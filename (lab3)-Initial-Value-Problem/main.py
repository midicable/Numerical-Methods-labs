from methods import backward_euler, runge_kutta, successive_order_boosting_second_order, extrapolation_adams_method

a, b = 1, 2
N = 10

u_e = backward_euler(a, b, N)
# u_r = runge_kutta(a, b, N)
# u_b = successive_order_boosting_second_order(a, b, N)
u_a = extrapolation_adams_method(a, b, N)

d = [0 for i in range(N + 1)]
for i in range(N + 1):
    d[i] = u_a[i] - u_e[i]
print(*d, sep='\n')