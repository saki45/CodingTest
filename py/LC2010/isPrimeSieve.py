def isPrimeSieve(n):
	isPrime = [1 for i in range(0, n+1)]

	import math
	sn = math.ceil(math.sqrt(n))

	for i in range(2, sn):
		if isPrime[i] == 1:
			print(i, end = ' ')
			j = 2*i
			while j <= n:
				isPrime[j] = 0
				j += i

	for i in range(sn, n+1):
		if isPrime[i] == 1:
			print(i, end = ' ')

	print()

if __name__ == '__main__':
	isPrimeSieve(200)
