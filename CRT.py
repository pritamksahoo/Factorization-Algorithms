import math
import numpy as np
from sympy.ntheory.factor_ import totient

if __name__ == '__main__':
	no = int(input("Enter no. of data : "))

	print("Enter a and m values [where, xi = ai (mod mi)] : ")

	data = []
	for i in range(no):
		print(str(i+1) + ") a" + str(i+1) + ", m" + str(i+1) + " :", end=' ')
		data.append(list(map(int, input().split())))

	print("\n============\nSolution :\n============\n")

	data = np.array(data)

	print("M = product of all modulos =", " * ".join(map(str, data[:, 1])), "=", end = " ")
	M = np.prod(data[:, 1])
	print(M, '\n')

	M_arr = M//data[:, 1]
	print("Now, ")
	for i in range(len(M_arr)):
		print("M" + str(i+1), "=", "M/m" + str(i+1), "=", M_arr[i])
	print()

	inv_M = [pow(int(M_arr[i]), totient(data[i][1]) - 1, int(data[i][1])) for i in range(len(M_arr))]
	print("Now, ")
	for i in range(len(M_arr)):
		print("M" + str(i+1) + "^(-1) (mod m" + str(i+1) + ") =", inv_M[i])
	print()

	ans = 0
	print("Now, x = (Summation of all (ai)*(Mi)*(Mi^(-1)) (mod M), for all i = 1(1)n\n")
	print("So, x =", end = " ")

	for i in range(len(M_arr)):
		if i == len(M_arr)-1:
			print(str(data[i][0]) + "*" + str(M_arr[i]) + "*" + str(inv_M[i]), "(mod " + str(M) + ")")
		else:
			print(str(data[i][0]) + "*" + str(M_arr[i]) + "*" + str(inv_M[i]) + " +", end = " ")
		ans = (ans + (int(data[i][0]) * int(M_arr[i]) * int(inv_M[i])) % M) % M

	print("\nSolution : x =", ans, "\n")
