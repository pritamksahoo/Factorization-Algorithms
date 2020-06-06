import math

if __name__ == '__main__':
	num = int(input("Enter the number : "))

	print("\n============\nSolution : \n============\n")
	start = math.ceil(num**0.5)
	print("[sqrt(" + str(num) + ")] = " + str(start))
	print("-------------\n")
	while True:
		print("t = " + str(start))
		print("t^2 - n = " + "(" + str(start) + ")^2 - " + str(num) + " =", end=' ')
		temp = start**2 - num
		print(temp, end=' ')

		if temp < 0:
			print("\nFactorization is not possible\n")
			break

		sqrt = int(temp**0.5)

		if temp == sqrt**2:
			print("= (" + str(sqrt) + ")^2")
			print("-------------")
			print("\nFactors found :", end=' ')
			print("(" + str(start) + " + " + str(sqrt) + ") = " + str(start+sqrt), "and", "(" + str(start) + " - " + str(sqrt) + ") = " + str(start-sqrt), '\n')
			break

		else:
			print('\n' + str(temp) + " is not a perfect square\n-------------\n")
			start = start + 1
