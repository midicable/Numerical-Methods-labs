from fredgolme_methods import fredgolme_mechanical_quadrature, fredgolme_successive_aproximations
from volterra_methods import volterra_mechanical_quadrature, volterra_successive_aproximations

a, b = 0, 1
N = 10
lambda_ = 1
n = 5

# Метод механических квадратур
u_fredgolme_mechanical_quadrature, u__fredgolme_mechanical_quadrature = fredgolme_mechanical_quadrature(a, b, N, lambda_)
u_volterra_mechanical_quadrature, u__volterra_mechanical_quadrature = volterra_mechanical_quadrature(a, b, N, lambda_)
print(f'Дискретные решения для ИУФ-2 и ИУВ-2 методом механических квадратур \n'
      f'--------------------------------------------------------------------')
print(f'Для уравнения Фредольма-2: {u_fredgolme_mechanical_quadrature}')
print(f'Значение в точке x*: {u__fredgolme_mechanical_quadrature}')
print('--------------------------------------------------------------------')
print(f'Для уравнения Вольтерры-2: {u_volterra_mechanical_quadrature}')
print(f'Значение в точке x*: {u__volterra_mechanical_quadrature}')
print('--------------------------------------------------------------------')

print()

# Метод последовательных приближений
u_fredgolme_successive_aproximations, u__fredgolme_successive_aproximations = fredgolme_successive_aproximations(a, b, N, lambda_, n)
u_volterra_successive_aproximations, u__volterra_successive_aproximations = volterra_successive_aproximations(a, b, N, lambda_, n)
print(f'Дискретные решения для ИУФ-2 и ИУВ-2 методом последовательных приближений \n'
      f'--------------------------------------------------------------------')
print(f'Для уравнения Фредольма-2: {u_fredgolme_successive_aproximations}')
print(f'Значение в точке x*: {u__fredgolme_successive_aproximations}')
print('--------------------------------------------------------------------')
print(f'Для уравнения Вольтерры-2: {u_volterra_successive_aproximations}')
print(f'Значение в точке x*: {u__volterra_successive_aproximations}')
print('--------------------------------------------------------------------')