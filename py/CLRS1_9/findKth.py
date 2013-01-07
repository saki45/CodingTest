def findKth(a, k):
	# k starts from 1
	if k <= 0 or k > len(a):
		print('illegal k!')
		return None

	st, ed = 0, len(a)-1
	while st <= ed:
		p = partitionList(a, st, ed)
		if p == k-1:
			return p,a[p]
		elif p > k-1:
			ed = p-1
		else:
			st = p+1

	return None

def partitionList(a, st, ed):
	if st == ed:
		return st

	p, q = st+1, st+1
	while q<=ed:
		if a[q] < a[st]:
			a[p], a[q] = a[q], a[p]
			p += 1
			q += 1
		else:
			q += 1
	
	a[st], a[p-1] = a[p-1], a[st]
	return p-1

if __name__ == '__main__':
	import random
	N = 12
	k = 8
	a = [int(random.uniform(0, 8*N)) for i in range(0, N)]
	print('a:',a)

	kp, kv = findKth(a, k)
	print('ours:', kp, kv)
	print(a)

	b = a[:]
	b.sort()
	print('answer:', b[k-1])

	
