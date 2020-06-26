from ec_addition import ec_fp_add as add 
import sys, os

def blockPrint():
	sys.stdout = open(os.devnull, 'w')

def enablePrint():
	sys.stdout = sys.__stdout__


if __name__ == '__main__':
	print("Equation of the elliptic curve : y^2 = x^3 + ax + b\nEnter the value of a and b :-")
	a = int(input("\ta : "))
	b = int(input("\tb : "))

	print("EC : y^2 = x^3", "+ " + str(a) + "x" if a != 0 else '', "+ " + str(b) if b != 0 else '')
	coeff = [1, a, b]

	prime = int(input("Enter the prime modulo : "))

	P = list(map(int, input("Enter P : ").split()))
	x = int(input("Enter private key x : "))

	blockPrint()
	Q = add(coeff, P, [x-1], prime)
	enablePrint()
	print("\nQ = xP =", Q, "\n")

	m = int(input("Enter message m (in Zp) : "))
	y = int(input("Enter random element y (in Zp) : "))

	blockPrint()
	yP = add(coeff, P, [y-1], prime)
	yQ = add(coeff, Q, [y-1], prime)
	enablePrint()

	print("\nyP :", yP, "& yQ :", yQ, "\n")

	hQ = int(input("Enter hash of yQ (in Zp) : "))

	C = [None, None]
	C[0] = (hQ + m)%prime
	print("\nC0 = (hQ + m) % prime =", C[0])
	C[1] = [yP[0], yP[1]%2]
	print("C1 = point-compress(yP) =", C[1])

	print("\n================\nCIPHER ::", C, "\n================\n")

	C1 = C[1]
	temp = C1[0]**3 + a*C1[0] + b
	temp = temp**((prime + 1)//4)
	temp1, temp2 = temp%prime, ((-1)*temp + prime)%prime

	print("C1 = decompress" + str(C[1]) + " =", end=' ')

	if temp1 % 2 == C1[1]:
		C1[1] = temp1
	else:
		C1[1] = temp2

	print(C1)
	print("Private key :", x)

	blockPrint()
	xC1 = add(coeff, C1, [x-1], prime)
	enablePrint()
	print("\nxC1 :", xC1)

	if xC1 == yQ:
		hC1 = hQ

	print("hC1 :", hC1)

	M = (C[0] - hC1 + prime) % prime
	print("M = (C[0] - hC1) % prime =", M)

	print("\n================\nMESSAGE ::", M, "\n================\n")