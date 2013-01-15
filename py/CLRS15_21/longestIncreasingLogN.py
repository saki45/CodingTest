def findLongestIncreasing(a):
	
	pass

def randomPermutation(a):
	
	import random
	for i in range(0, len(a)):
		j = int(random.uniform(i, len(a)))
		a[i], a[j] = a[j], a[i]


if __name__ == '__main__':
	
	N = 10
	a = [i for i in range(1, N)]
	randomPermutation(a)
	print(a)
