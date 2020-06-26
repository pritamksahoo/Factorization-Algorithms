import math
from sympy.ntheory.factor_ import totient

if __name__ == '__main__':
	a, m = list(map(int, input("Enter number and modulo : ").split()))

	assert(math.gcd(a,m) == 1)

	phi = totient(m)

	for i in range(1, phi+1):
		if phi%i == 0:
			if pow(a,i,m) == 1:
				break

	print("\nORD(a) =", i, "(mod m)\n")