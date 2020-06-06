import numpy as np
import math

def pollard_rho(num, degree, coeff, x0):
	x = [x0]
	ans = None
	last_exp = 1
	print("x0 =", str(x0), '\n-----------')

	i, k = 1, 0
	while True:
		prev_x = x[i-1]
		new_x = 0

		print("\nx" + str(i) + " =", end=' ')
		for j in range(0, degree+1):
			if coeff[j] != 0:
				if j < degree-1:
					print((str(coeff[j]) if coeff[j] > 1 else ' ') + "x" + str(i-1) + "^" + str(degree-j) + (' +' if j < degree else ' '), end=' ')
				elif j == degree-1:
					print((str(coeff[j]) if coeff[j] > 1 else ' ') + "x" + str(i-1) + (' +' if j < degree else ' '), end=' ')
				else:
					print(str(coeff[j]), end=' ')
			new_x = (new_x + coeff[j]*(prev_x**(degree-j))) % num

		x.append(new_x)
		print("\nx" + str(i) + " =", str(new_x), "(mod", str(num) + ")", '\n')

		if i == 1:
			k = 0

		elif i >= 2**(last_exp):
			last_exp = last_exp + 1
			k = 2**(last_exp - 1) - 1

		ans = math.gcd(abs(x[k]-new_x), num)

		print("\tgcd(x" + str(i) + " - x" + str(k) + ", " + str(num) + ")", end=' ')
		print("= gcd(" + str(x[i] - x[k]) + ", " + str(num) + ") = " + str(ans))
		print('-----------')

		if ans > 1:
			print("\nFactor found : " + str(ans) + '\n')
			break
		else:
			i = i + 1

	return ans

if __name__ == '__main__':
	num = int(input("Enter the number : "))

	print("\nEnter polynomial details : ")

	degree = int(input("Degree : "))
	print("Polynomial of the form :", end=' ')

	for d in range(degree):
		print("a" + str(d) + "x^" + str(degree-d) + " + ", end=' ')

	print("a" + str(degree))
	print("Enter the coefficients (space-seperated) :", end=' ')

	coeff = list(map(int, input().split()))

	x0 = int(input("Enter the starting value (x0) : "))

	print("\n=================\nSolution : \n=================\n")
	factor = pollard_rho(num, degree, coeff, x0)
