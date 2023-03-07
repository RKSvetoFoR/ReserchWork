import math


def first_newton(nodes, diff_table, int_point) -> float:
	numerator = 1.0
	result = diff_table[0]

	h = (nodes[1].x-nodes[0].x)
	t = (int_point - nodes[0].x)/h

	for i in range(1, len(nodes)):

		for j in range(1, i+1):
			numerator *= t - j + 1

		result += (numerator*diff_table[i]/math.factorial(i))

		numerator = 1.0

	return result


def second_newton(nodes, diff_table, int_point) -> float:
	numerator = 1.0
	result = diff_table[0]

	h = (nodes[1].x-nodes[0].x)
	t = (int_point - nodes[-1].x)/h

	for i in range(1, len(nodes)):

		for j in range(1, i+1):
			numerator *= t + j - 1

		result += (numerator*diff_table[i]/math.factorial(i))

		numerator = 1.0

	return result
