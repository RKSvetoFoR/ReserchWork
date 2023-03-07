from os import system

import matplotlib.pyplot as plt

from Lab3._Data import getDataSet
from Lab3.additional_info import PATH
from Lab3.Lagrange import Lagrange
from Lab3.NewtonFormulas import first_newton, second_newton


def Lagrange_Newton(nodes):
    inter_point = float(input("Enter interpolate point : "))
    x = [i.x for i in nodes]
    y = [i.f for i in nodes]
    diff_table = list([y])
    diff_nf = [y[0]]
    diff_nb = [y[-1]]

    for i in range(len(nodes) - 1):
        temp_diff = []
        for j in range(len(diff_table[i]) - 1):
            temp_diff.append(diff_table[i][j + 1] - diff_table[i][j])
        diff_table.append([round(i, 3) for i in temp_diff])
        diff_nf.append(round(temp_diff[0], 3))
        diff_nb.append(round(temp_diff[-1], 3))

    for i in diff_table:
        print(i)

    if inter_point < float(nodes[int(len(nodes) / 2)].x):

        print("First Newton")
        # print(diff_nf)
        print("Result : ", round(first_newton(nodes=nodes,
                                              diff_table=diff_nf, int_point=inter_point), 3))

        plt.plot(x, y)
        plt.scatter(inter_point, round(first_newton(nodes=nodes,
                                                    diff_table=diff_nf, int_point=inter_point), 3), color="red")
        plt.legend('Первый Ньютон')
        plt.show()
    else:

        print("Second_Newton")
        # print(diff_nb)
        print("Result : ", round(second_newton(nodes=nodes,
                                               diff_table=diff_nb, int_point=inter_point), 3))

        plt.plot(x, y)
        plt.scatter(inter_point, round(second_newton(nodes=nodes,
                                                     diff_table=diff_nb, int_point=inter_point), 3), color="red")
        plt.legend('Второй Ньютон')
        plt.show()

    print("Lagrange:")
    pnt = (Lagrange(nodes, inter_point))
    print(pnt)
    plt.plot(x, y)
    plt.scatter(inter_point, pnt, color="red")
    plt.legend('Лагранж')
    plt.show()


def main():
    nodes = getDataSet(path=PATH)
    Lagrange_Newton(nodes=nodes)


if __name__ == '__main__':
    system('cls')
    main()
