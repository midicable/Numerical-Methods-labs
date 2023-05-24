from lab.methods import solve_heat_equation
from additional.plotter import plot

if __name__ == '__main__':
    u_exact_full_matrix = solve_heat_equation(0.005, 0.00025)
    u_exact = []
    print(len(u_exact_full_matrix[0]))
    for i in range(0, len(u_exact_full_matrix), 200):
        u_exact.append([u_exact_full_matrix[i][j] for j in range(0, 201, 10)])

    u_lab_full_matrix = solve_heat_equation(0.05, 0.0025)
    u_lab = [u_lab_full_matrix[i] for i in range(0, 401, 20)]

    print('solution:')
    for i in range(len(u_exact) - 1, -1, -1):
        for j in range(len(u_exact[0])):
            print('%.6f' % u_lab[i][j], end=' ')
        print()

    # "Exact" solution (implicit scheme with weights σ=1/4)
    # "Exact" solution (implicit scheme with weights σ=1/4) Δt=5s