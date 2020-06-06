import numpy as np
import math

def pollard_rho(num, degree, coeff, x0):
	x = [x0]
	ans = None

	print("x0 =", str(x0), '\n-----------')

	i = 1
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

		j = i-1
		while j >= 0 and math.gcd(abs(x[j]-new_x), num) == 1:
			print("\tgcd(x" + str(i) + " - x" + str(j) + ", " + str(num) + ")", end=' ')
			print("= gcd(" + str(x[i] - x[j]) + ", " + str(num) + ") = " + str(math.gcd(abs(x[j]-new_x), num)))
			j = j-1

		if j >= 0:
			ans = math.gcd(abs(x[j]-new_x), num)
			print("\tgcd(x" + str(i) + " - x" + str(j) + ", " + str(num) + ")", end=' ')
			print("= gcd(" + str(x[i] - x[j]) + ", " + str(num) + ") = " + str(ans))
			print('-----------')
			print("\nFactor found : " + str(ans) + '\n')
			break
		else:
			i = i + 1

		print('-----------')

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
