def quickSort(a, st, ed):
	if st >= ed:
		return

	p = partition(a, st, ed)
	quickSort(a, st, p-1)
	quickSort(a, p+1, ed)

def partition(a, st, ed):
	p, q = st+1, ed
	while p <= q:
		if a[p] <= a[st]:
			p += 1
		else:
			tmp = a[q]
			a[q] = a[p]
			a[p] = tmp
			q -= 1
	tmp = a[st]
	a[st] = a[p-1]
	a[p-1] = tmp
	return p-1
	
