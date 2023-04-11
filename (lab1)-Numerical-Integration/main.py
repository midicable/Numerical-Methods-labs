from functions import runge_rule, trapezoid_formula,\
    simpsons_formula, gauss_quadrature_formula, gauss_quadrature_remainder

a, b = 0.2, 0.3
eps = 0.00001
integral_exact_value = 0.12101312327

Q_runge, h_runge = runge_rule(a, b, eps)
Q_trapezoid, h_trapezoid = trapezoid_formula(a, 0.02, 5), 0.02
Q_simpson, h_simpson = simpsons_formula(a, 0.05, 2), 0.05
Q_gauss = gauss_quadrature_formula()

print('-------------------------------')
print('Runge rule results:')
print(f'Q = {Q_runge}, h = {h_runge}')
print(f'I - Q = {round(integral_exact_value - Q_runge, 10)}')
print('-------------------------------')
print('Trapezoid results:')
print(f'Q = {Q_trapezoid}, h = {h_trapezoid}')
print(f'I - Q = {round(integral_exact_value - Q_trapezoid, 10)}')
print('-------------------------------')
print('Simpson formula results:')
print(f'Q = {Q_simpson}, h = {h_simpson}')
print(f'I - Q = {round(integral_exact_value - Q_simpson, 10)}')
print('-------------------------------')
print('Gauss formula results:')
print(f'Q = {Q_gauss}')
print(f'I - Q = {round(integral_exact_value - Q_gauss, 10)}')
print(f'R = {round(gauss_quadrature_remainder(), 10)}')
print('-------------------------------')

