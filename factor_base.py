import math
import numpy as np
import random

def gen_prime_upto_n(limit):
	arr = [True for i in range(limit+1)]

	start = 2

	while start <= limit:
		if not arr[start]:
			start = start + 1
			continue

		mult_unit = 2

		while (start*mult_unit) <= limit:
			arr[start*mult_unit] = False
			mult_unit = mult_unit + 1

		start = start + 1

	return arr

def lar(x, n):
	r = (x**2)%n

	if r > (n//2):
		r = r - n

	return r

def repr_b_number(n, p):
	v = [0 for i in range(len(p))]

	if n < 0:
		v[0] = 1
		n = n * (-1)

	for ind, prime in enumerate(p):
		if ind == 0:
			continue

		p_count = 0
		while n%prime == 0 and n != 1:
			p_count = p_count + 1
			n = n//prime

		v[ind] = p_count

		if n == 1:
			break

	if n != 1:
		return None

	else:
		return v

if __name__ == '__main__':
	num = int(input("Enter the number : "))

	prime_limit = int(input("Enter prime limit : "))
	prime_arr = gen_prime_upto_n(prime_limit)

	B = [-1]

	print("\nB-Primes :", end=' ')
	print("-1", end=' ')

	for i in range(2, prime_limit+1):
		if prime_arr[i]:
			print(str(i), end=' ')
			B.append(i)

	print()

	k, done, count_b = 1, False, 0
	vectors = {}

	while not done:
		sqrt = int((k*num)**0.5)
		b1, b2, k = sqrt, sqrt + 1, k + 1
		#print(b1, b2)
		r1, r2 = lar(b1, num), lar(b2, num)
		#print(r1, r2)
		repr1 = repr_b_number(r1, B)
		repr2 = repr_b_number(r2, B)
		#print(repr1, repr2)
		if repr1 is not None:
			vectors[b1] = repr1
			count_b = count_b + 1

		if repr2 is not None:
			vectors[b2] = repr2
			count_b = count_b + 1
		#print(count_b)
		if count_b > len(B) + 1:
			done = True

	print("\nEntire B-table : \n")
	print("    b   b^2", end='')

	for p in B:
		print("%5d" % (p), end='')

	print()

	for k in vectors:
		for i in range(3*(prime_limit+1)):
			print("-", end='')

		print()
		print("%5d %5d" % (k, lar(k, num)), end='')

		v = vectors[k]
		for el in v:
			print("%5d" % (el), end='')

		print()

	print()

	done = False
	bs = sorted(list(vectors.keys()))

	while not done:
		n = np.random.randint(2, len(vectors))
		#ns = np.random.randint(0, len(vectors), n)
		ns = random.sample(range(0, len(vectors)), n)

		done = True
		alpha = []
		for i in range(len(B)):
			prime = B[i]

			summ = 0
			for v in ns:
				summ = summ + vectors[bs[v]][i]

			if summ%2 != 0:
				done = False
				break
			else:
				alpha.append(summ//2)

	if done:

		print("Chosen b's :", end = ' ')

		t = 1
		for v in ns:
			print(bs[v], end=' ')
			t = (t * bs[v]) % num

		print("\n")
		print("t = product of all b's = " + str(t) + " (mod " + str(num) + ")\n")

		s = 1
		print("s = (product of all primes on the r.h.s of all b's) ^ (1/2) =", end=' ')
		for ind, prime in enumerate(B):
			if alpha[ind] >= 1:
				print("(" + str(prime) + ")^" + str(alpha[ind]) + " *", end = ' ')
			s = (s * (prime**alpha[ind])) % num

		print(1, "=", s, "(mod " + str(num) + ")")

		if s == t or s == (-1)*t:
			print("\nBut, s = +- t (mod " + str(num) + ")")
			print("\nFailed\n")

		else:
			print("\ns != +- t (mod " + str(num) + ")")
			print("\nFactor found :", end=' ')
			print("gcd(s+t, " + str(num) + ") =", math.gcd(s+t, num), "and", "gcd(s-t, " + str(num) + ") =", math.gcd(s-t, num), '\n')
