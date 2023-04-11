from lab.methods import form_matrix_1, form_matrix_2, form_matrix_3
from linalg.methods import tridiagonal_method


def main():
    N = 10
    N_HP = 1000

    A_1, B_1, C_1, F_1 = form_matrix_1(N)
    y_1 = tridiagonal_method(A_1, B_1, C_1, F_1, N)

    A_2, B_2, C_2, F_2 = form_matrix_2(N)
    y_2 = tridiagonal_method(A_2, B_2, C_2, F_2, N)

    A_3, B_3, C_3, F_3 = form_matrix_3(N)
    y_3 = tridiagonal_method(A_3, B_3, C_3, F_3, N)

    A, B, C, F = form_matrix_1(N_HP)
    y_high_precision_full_array = tridiagonal_method(A, B, C, F, N_HP)
    y_high_precision = [y_high_precision_full_array[i] for i in range(0, N_HP + 1, int(N_HP / 10))]

    print('Решение точное')
    for i in range(len(y_high_precision)):
        print('%.6f' % y_high_precision[i])
    print()

    print('Решение, полученное разностной аппроксимацией дифференциального оператора:')
    for i in range(len(y_1)):
        print('%.6f' % y_1[i])
    print()
    print('Невязка при разностной аппроксимацией дифференциального оператора:')
    for i in range(len(y_1)):
        print('%.6f' % (y_high_precision[i] - y_1[i]))
    print()

    print('Решение, полученное интегро-интерполяционным методом:')
    for i in range(len(y_2)):
        print('%.6f' % y_2[i])
    print()
    print('Невязка при интегро-интерполяционном методе:')
    for i in range(len(y_2)):
        print('%.6f' % (y_high_precision[i] - y_2[i]))
    print()

    print('Решение, полученное вариационно-разностным методом Ритца:')
    for i in range(len(y_3)):
        print('%.6f' % y_3[i])
    print()
    print('Невязка при вариационно-разностном методе Ритца:')
    for i in range(len(y_3)):
        print('%.6f' % (y_high_precision[i] - y_3[i]))
    print()



if __name__ == '__main__':
    main()

