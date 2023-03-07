import numpy as np


def Thomas_Algorithm(matrixA: np.array, matrixY: list, n: int) -> np.array:
	n -= 2
	coefficent_C = np.zeros(n)
	kappa = matrixA[0][0]
	alpha = [-matrixA[0][1]/kappa]
	beta = [matrixY[0]/kappa]

	for i in range(1, n):

		kappa = matrixA[i][i] + matrixA[i][i-1] * alpha[i-1]

		if i != n-1:
			alpha.append(- matrixA[i][i + 1] / kappa)

		beta.append((matrixY[i] - matrixA[i][i-1] * beta[i-1]) / kappa)

	coefficent_C[n-1] = beta[n-1]

	for i in range(n-2, -1, -1):
		coefficent_C[i] = alpha[i]*coefficent_C[i+1] + beta[i]

	coefficent_C = np.append(coefficent_C, 0)
	coefficent_C = np.insert(coefficent_C, 0, 0)

	return coefficent_C


def find_coeff_D(coeffC: np.array, h: float, n: int):
	coeffD = np.zeros(n)

	for i in range(1, n):
		coeffD[i] = (coeffC[i] - coeffC[i-1])/h

	return coeffD


def find_coeff_B(nodes: np.array, coeffC: np.array, coeffD: np.array, h: float,  n: int):
	coeffB = np.zeros(n)

	for i in range(1, n):
		coeffB[i] = h/2.*coeffC[i] - \
			((h**2)*coeffD[i])/6 + (nodes[i].f - nodes[i-1].f)/h

	return coeffB
