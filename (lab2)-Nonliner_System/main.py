from methods import*
import numpy as np

X_Gauss_Seidel, Y_Gauss_Seidel, Iterations_Gauss_Seidel = GaussSeidelMethod(3, 0.5, 10**(-7))
X_Secant_Method, Y_Secant_Method, Iterations_Secant_Method = SecantMethod(3, 0.5, 10**(-7))

print('Gauss Seidel Results:')
print(f'(x, y) = ({X_Gauss_Seidel}, {Y_Gauss_Seidel})')
print('f1(x*, y*) =', func1(X_Gauss_Seidel, Y_Gauss_Seidel), sep=' ')
print('f2(x*, y*) =', func2(X_Gauss_Seidel, Y_Gauss_Seidel), sep=' ')
print('||(f1(x*, y*), f2(x*, y*))|| =', np.linalg.norm([func1(X_Gauss_Seidel, Y_Gauss_Seidel),
                                                         func2(X_Gauss_Seidel, Y_Gauss_Seidel)], np.inf))
print('iterations =', Iterations_Gauss_Seidel)

print()

print('Secant Method Results:')
print(f'(x, y) = ({X_Secant_Method}, {Y_Secant_Method})')
print('f1(x*, y*) =', func1(X_Secant_Method, Y_Secant_Method), sep=' ')
print('f2(x*, y*) =', func2(X_Secant_Method, Y_Secant_Method), sep=' ')
print('||(f1(x*, y*), f2(x*, y*))|| =', np.linalg.norm([func1(X_Secant_Method, Y_Secant_Method),
                                                         func2(X_Secant_Method, Y_Secant_Method)], np.inf))
print('iterations =', Iterations_Secant_Method)





