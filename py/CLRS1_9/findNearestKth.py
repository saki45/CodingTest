from findKth import findKth

def findNearestKth(a, n, k):
	# This method returns the nearest k elements along with the nth largest element
	if n >= len(a):
		print('illegal n')
		return None

	p, v = findKth(a, n)
	print(v)
	if k == 0:
		return v

	if k < 0:
		k = -k

	# p -- the kth nearest element to a[n]
	# a[:p+1] all the needed (2k+1) elements including a[n]
	p = findKthNear(a, v, 2*k+1)
	return a[:p+1]

def findKthNear(a, v, k):
	st, ed, ck = 0, len(a)-1, k

	while st <= ed:
		if st == ed:
			return st

		# compares the difference of each elements and v
		p = partitionNearest(a, v, st, ed)
		if p == ck-1:
			return p
		elif p > ck-1:
			ed = p-1
		else:
			st = p+1
	
def partitionNearest(a, v, st, ed):
	p, q = st+1, st+1
	d0 = abs(a[st] - v)

	while q <= ed:
		if abs(a[q]-v) >= d0:
			q += 1
		else:
			a[p], a[q] = a[q], a[p]
			p += 1
			q += 1

	a[st], a[p-1] = a[p-1], a[st]
	return p-1

if __name__ == '__main__':

	import random
	N = 12
	n = 6
	k = 2
	a = [int(random.uniform(0, 4*N)) for i in range(0, N)]

	print(a)
		
	b = findNearestKth(a, n, k)
	print('ours:',b)

	a.sort()
	print(a)
