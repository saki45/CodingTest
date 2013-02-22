# the problem is to count the total occurance of digit '1' from number 1 to N
# here I will implement two different methods, the first one is the naive mathod, and the second one is more elegant

def countOnesNaive(N):
	# This is the naive method, we just scan from 1 to n, and summing up all the ones occurred within each number
	if N<=0:
		return

	oneCount = 0
	for num in range(1, N+1):
		oneCount += getOnesInNum(num)

	print(oneCount)

def getOnesInNum(num):
	oneCount = 0

	while num>0:
		lastDigit = num%10
		if lastDigit == 1:
			oneCount += 1
		num = num // 10
	return oneCount

def getDigits(N):
	# This method get the number of digits of a given positive number N:
	if N<=0:
		return 0

	digitCount = 0
	while N>0:
		N = N // 10
		digitCount += 1
	return digitCount

def getTotal(digit):
	# This methods calculate the number of occurance of ones within all the numbers between 1 to 10^digit-1
	return digit*10**(digit-1)

def countOnes(N):
	oneCount = 0
	# The basic idea of the elegant method is to divide the numbers into different subgroups
	while N>0:
		digit = getDigits(N)
		if digit == 1:
			oneCount += 1
			N = 0
		else:
			highestDigit = N // (10**(digit-1))
			# Adding up all the ones in the groups with all numbers with (digit-1) digits
			# e.g.  for 32345, we divide the groups like 0-9999, 10000-19999, 20000-29999, 30000-39999
			# for each 0-9999, the occurance of ones are calculated via getTotal(4)
			oneCount += highestDigit * getTotal(digit-1)
			N = N - highestDigit * 10**(digit-1)

			# adding up the ones in the highest digit
			if highestDigit == 1:
				oneCount += N+1
			else:
				oneCount += 10**(digit-1)

	print(oneCount)


def testTwoMethods(N):
	# This method is used to compare the result and the running time of two methods
	print("\nCounting ones from 1 to ", N, sep='')
	print("Naive method: ", end='')
	elps = time.time()
	countOnesNaive(N)
	elps = time.time() - elps
	print("Elapsed time: ", elps, sep='')
	print("Elegant method: ", end='')
	elps = time.time()
	countOnes(N)
	elps = time.time() - elps
	print("Elapsed time: ", elps, sep='')


if __name__ == "__main__":

	import time

	testTwoMethods(4)
	testTwoMethods(10)
	testTwoMethods(99)
	testTwoMethods(35124)
	testTwoMethods(130216)
