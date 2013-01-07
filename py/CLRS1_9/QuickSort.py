import random

def printList(a):
	for i in a:
		print(i, end=' ')
	print()

def quickSort(a, st, ed):
	if st >= ed:
		return

	p = partition(a, st, ed)
	quickSort(a, st, p-1)
	quickSort(a, p+1, ed)

def partition(a, st, ed):
	idx = int(random.uniform(st, ed+1))
	a[st], a[idx] = a[idx], a[st]
	p, q = st+1, ed
	while p <= q:
		if a[p] <= a[st]:
			p += 1
		else:
			a[p], a[q] = a[q], a[p]
			q -= 1
	tmp = a[st]
	a[st] = a[p-1]
	a[p-1] = tmp
	return p-1
	
def quickSortE(a, st, ed):
	if st >= ed:
		return

	# a[st, p] < a[p+1, q-1] < a[q, ed]
	#  <pivot       =pivot     > pivot
	p, q = partitionE(a, st, ed)
	print(p, q, st, ed)
	printList(a)
	quickSortE(a, st, p)
	quickSortE(a, q, ed)

def partitionE(a, st, ed):
	p, q, r = st+1, st+1, st+1
	while r <= ed:
		if a[r] > a[st]:
			r += 1
		elif a[r] == a[st]:
			a[r], a[q] = a[q], a[r]
			r += 1
			q += 1
		else:
			tmp = a[r]
			a[r] = a[q]
			a[q] = a[p]
			a[p] = tmp
			r += 1
			q += 1
			p += 1
	a[st], a[p-1] = a[p-1], a[st]	
	# p-1 .. q-1  equal to pivot
	return p-2, q
