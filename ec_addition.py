import math
from sympy.ntheory.factor_ import totient

def ec_add(coeff, p1, p2):
	ans = [0, 0]

	if len(p2) == 2:
		print("P(x1, y1) + Q(x2, y2) = R(x3, y3)\n")

		if p1 != p2:
			slope = (p2[1] - p1[1]) / (p2[0]- p1[0])
			print("lambda = (y2-y1)/(x2-x1) =", "(" + str(p2[1]) + " - " + str(p1[1]) + ")/(" + str(p2[0]) + " - " + str(p1[0]) + ") =", str(slope))
		else:
			slope = (3*(p1[0]**2) + coeff[1]) / (2*p1[1])
			print("lambda = (3(x1^2) + a)/2y1 =", "(3 * " + "(" + str(p1[0]) + "^2 + " + str(coeff[1]) + ") / (2 * " + str(p1[1]) + ") =", str(slope))

		ans[0] = slope**2 - p1[0] - p2[0]
		print("x3 = (lambda^2 - x1 - x2) =", "(" + str(slope) + "^2 - " + str(p1[0]) + " - " + str(p2[0]) + ") =", str(ans[0]))

		ans[1] = slope*(p1[0] - ans[0]) - p1[1]
		print("y3 = (lambda(x1 - x3) - y1) =", "(" + str(slope) + " * (" + str(p1[0]) + " - " + str(ans[0]) + ") - " + str(p1[1]) + ") =", str(ans[1]))

		print("\nAddition :", str(tuple([ans[0], ans[1]])))
		return ans
	else:
		freq = p2[0]
		p2 = p1.copy()

		for i in range(freq):
			print("\n----------------")
			p2 = ec_add(coeff, p1, p2)
			print("----------------")

		print("\nResult :", str(tuple([p2[0], p2[1]])))
		return p2

def ec_fp_add(coeff, p1, p2, prime):
	ans = [0, 0]

	if len(p2) == 2:
		print("P(x1, y1) + Q(x2, y2) = R(x3, y3)\n")

		if p1 != p2:
			slope = ((p2[1] - p1[1]) * pow((p2[0]- p1[0]), prime-2, prime)) % prime
			print("lambda = (y2-y1)*((x2-x1)^-1) =", "(" + str(p2[1]) + " - " + str(p1[1]) + ")*(" + str(p2[0]) + " - " + str(p1[0]) + ")^-1 =", str(slope) + " (mod " + str(prime) + ")")
		else:
			slope = ((3*(p1[0]**2) + coeff[1]) * pow((2*p1[1]), prime-2, prime)) % prime
			print("lambda = (3(x1^2) + a) * (2y1)^-1 =", "(3 * " + "(" + str(p1[0]) + "^2 + " + str(coeff[1]) + ") * (2 * " + str(p1[1]) + ")^-1 =", str(slope) + " (mod " + str(prime) + ")")

		ans[0] = (slope**2 - p1[0] - p2[0]) % prime
		print("x3 = (lambda^2 - x1 - x2) =", "(" + str(slope) + "^2 - " + str(p1[0]) + " - " + str(p2[0]) + ") =", str(ans[0]) + " (mod " + str(prime) + ")")

		ans[1] = (slope*(p1[0] - ans[0]) - p1[1]) % prime
		print("y3 = (lambda(x1 - x3) - y1) =", "(" + str(slope) + " * (" + str(p1[0]) + " - " + str(ans[0]) + ") - " + str(p1[1]) + ") =", str(ans[1]) + " (mod " + str(prime) + ")")

		print("\nAddition :", str(tuple([ans[0], ans[1]])))
		return ans
	else:
		freq = p2[0]
		p2 = p1.copy()

		for i in range(freq):
			print("\n----------------")
			p2 = ec_fp_add(coeff, p1, p2, prime)
			print("----------------")

		print("\nResult :", str(tuple([p2[0], p2[1]])))
		return p2

if __name__ == '__main__':
	print("Equation of the elliptic curve : y^2 = x^3 + ax + b\nEnter the value of a and b :-")
	a = int(input("\ta : "))
	b = int(input("\tb : "))

	print("EC : y^2 = x^3", "+ " + str(a) + "x" if a != 0 else '', "+ " + str(b) if b != 0 else '')
	coeff = [1, a, b]

	prime = int(input("Enter the prime modulo (-1 if EC is not defined over Zp) : "))

	point1 = list(map(int, input("\nEnter first point(P, x and y coordinates space-separted) : ").split()))
	point2 = input("Enter the second point (leave blank if same as first point) : ")

	if point2 == "":
		freq = int(input("How many times do you want to add " + str(tuple(point1)) + " to itself? : "))
		point2 = [freq]
	else:
		point2 = list(map(int, point2.split()))

	print("\n==============\nSolution : \n==============\n")
	if prime < 0:
		ec_add(coeff, point1, point2)
	else:
		ec_fp_add(coeff, point1, point2, prime)
	print()
