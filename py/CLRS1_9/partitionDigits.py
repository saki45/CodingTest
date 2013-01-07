# this method partitions an integer array a according to the last digit
def partitionDigits(a):
	p = [0] * 10
	while p[9] < len(a):
		processOneElement(a, p)
		

def processOneElement(a, p):
	idx = a[p[9]] % 10
	i = 9
	tmp = a[p[9]]
	while i > idx :
		a[p[i]] = a[p[i-1]]
		p[i] += 1
		i -= 1

	a[p[idx]] = tmp
	p[idx] += 1

if __name__ == '__main__':
	import random
	N = 50
	a = [int(random.uniform(0, 100)) for i in range(0, N)]

	print(a)
	print()
	partitionDigits(a)
	print(a)
