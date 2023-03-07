from os import system

import matplotlib.pyplot as plt

from _Data import getDataSet
from _FillMatrix import fill_matrix_A, fill_matrix_y
from _FindCoefficent import Thomas_Algorithm, find_coeff_B, find_coeff_D
from additional_info import PATH


def Cubic_Spline(nodes):
    x_ = [i.x for i in nodes]
    y_ = [i.f for i in nodes]

    h = 1  # round((nodes[-1].x-nodes[0].x)/len(nodes), 1)  # step

    A = fill_matrix_A(n=int(len(nodes)), h=h)
    y = fill_matrix_y(nodes=nodes, h=h)

    coeff_C = Thomas_Algorithm(matrixA=A, matrixY=y, n=len(nodes))
    print(coeff_C)
    coeff_D = find_coeff_D(coeffC=coeff_C, h=h, n=len(nodes))
    print(coeff_D)
    coeff_B = find_coeff_B(nodes=nodes, coeffC=coeff_C,
                           coeffD=coeff_D, h=h, n=len(nodes))
    print(coeff_B)

    dx = x_[0]
    h_spline = h / (len(nodes) - 1)

    x_spline = []
    y_spline = []

    for i in range(len(nodes)):
        while dx <= x_[i]:
            x_spline.append(dx)
            y_spline.append(nodes[i].f + coeff_B[i] * (dx - x_[i]) +
                            coeff_C[i] / 2 * (dx - x_[i]) ** 2 + coeff_D[i] / 6 * (dx - x_[i]) ** 3)
            dx += h_spline

    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title('Source')
    ax1.plot(x_, y_, color='green')
    ax1.scatter(x_, y_, color='black')
    ax2.set_title('Interpolated')
    ax2.plot(x_spline, y_spline, color='red')

    plt.show()


def main():
    nodes = getDataSet(path=PATH)
    Cubic_Spline(nodes=nodes)


if __name__ == '__main__':
    system('cls')
    main()
