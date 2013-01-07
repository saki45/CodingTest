def findJointKthWrap(a, b, k):

	# find the kth element in the sorted list a and b
	# k starts from 1 instead of 0

	if not len(a) == len(b):
		print('length not equal!')
		return None
	if len(a)*2 < k or k < 1:
		print('Illeagal k!')
		return None

	p = findJointKth(a, b, k) #returns the index
	if not p == None:
		return a[p]
	p = findJointKth(b, a, k)
	return b[p]
	
def findJointKth(a, b, k):

	# iteratively find the kth element 
	# condition: b[k-p-2] <= a[p] <= b[k-p-1]
	#              k-p-1       p

	if a[k-1] <= b[0]:
		return a[k-1]

	st, ed = 0, k-1
	while st <= ed:
		p = (st+ed)//2
		if b[k-p-2] <= a[p] <= b[k-p-1]:
			return p
		if a[p] < b[k-p-2]:
			st = p+1
		if a[p] > b[k-p-1]:
			ed = p-1

	return None

if __name__ == '__main__':
	N = 12

	import random

	a = [int(random.uniform(0, 6*N)) for i in range(0, N)]
	b = [int(random.uniform(0, 6*N)) for i in range(0, N)]
	
	a.sort()
	b.sort()

	print('a:', a)
	print('b:', b)

	k = 8
	ok = findJointKthWrap(a, b, k)
	print('our kth:', ok)
	
	c = a+b
	c.sort()
	print('answer', c[k-1])
