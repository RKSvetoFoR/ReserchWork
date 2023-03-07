import numpy as np


def fill_matrix_A(n: int, h: float) -> np.array:
	#
	#   fill tripple diagonla matrix
	#   where n - size square matrix
	#         h - spline step split
	#

	n -= 2
	matrix = np.zeros((n, n))

	for i in range(0, n):
		matrix[i][i] = 4*h
		matrix[i-1][i] = float(h)
		matrix[i][i-1] = float(h)

	# matrix[0][len(matrix)-1] = 0.
	# matrix[len(matrix)-1][0] = 0.

	return matrix


def fill_matrix_y(nodes, h: int) -> list:
	y = list()
	for i in range(1, len(nodes)-1):
		y.append(6*((nodes[i+1].f-nodes[i].f)/h - (nodes[i].f-nodes[i-1].f)/h))

	return y
