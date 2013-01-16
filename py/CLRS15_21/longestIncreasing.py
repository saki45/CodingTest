def findLongestIncreasingLogN(a):

	# find longest increasing sublist in O(n log n)

	length = [-1 for i in range(1, len(a))]
	past = [-1 for i in range(0, len(a))]

	length[0] = 0
	cur_longest = 0

	for i in range(1, len(a)):

		if a[i] > a[length[cur_longest]]:
			past[i] = length[cur_longest]
			cur_longest += 1
			length[cur_longest] = i

		elif a[i] < a[length[0]]:
			length[0] = i


		else:
			idx = myBinSearch(a, length, cur_longest, a[i])
			
			# idx is the index that length[idx] < a[i] < length[idx+1]

			length[idx+1] = i
			past[i] = length[idx]

	printResult(a, past, length[cur_longest])
	print()
	

def myBinSearch(a, length, cur_longest, key):

	st, ed = 0, cur_longest
	mid = (st+ed)//2

	while st <= ed:
		if a[length[mid]] < key < a[length[mid+1]]:
			return mid

		elif a[length[mid+1]] < key:
			st = mid + 1

		else:
			ed = mid - 1
		mid = (st+ed)//2 


def findLongestIncreasing(a):

	# find longest increasing sublist in O(n^2)

	length = [1 for i in range(0, len(a))]
	past = [-1 for i in range(0, len(a))]

	for i in range(1, len(a)):
		for j in range(0,i):

			if a[i] >= a[j] and length[i] < length[j]+1:

				length[i] = length[j] + 1
				past[i] = j

	printResult(a, past, length.index(max(length)))
	print()


def printResult(a, past, l):

	if past[l] is -1:
		print(a[l], end = " ")
		return

	printResult(a, past, past[l])
	print(a[l], end = " ")
	


def randomPermutation(a):
	
	import random
	for i in range(0, len(a)):
		j = int(random.uniform(i, len(a)))
		a[i], a[j] = a[j], a[i]


if __name__ == '__main__':
	
	N = 20
	a = [i for i in range(1, N)]
	randomPermutation(a)
	print(a)

	print("O(n^2) algorithm: ")
	findLongestIncreasing(a)
	print("O(n log n) algorithm: ")
	findLongestIncreasingLogN(a)
