import random
a = []
N = 8
n = 0
while n<N:
	a.append(int(random.uniform(3*N,1)))
	n += 1

def printArray(a):
	for i in a:
		print(i,end=' ')
	print()

b = a[:]
print(len(a))
printArray(a)
printArray(b)

def merge(a, b, st, ed):
	mid = int((st+ed)/2)
	p, q, r = (st, mid+1, st)
	while(p<=mid and q<=ed):
		if(a[p] <= a[q]):
			b[r] = a[p]
			r += 1
			p += 1
		else:
			b[r] = a[q]
			q += 1
			r += 1
	print(st, ed, ':')
	print(p, q, r)
	if(p<=mid):
		b[r:ed+1] = a[p:mid+1]
	elif(q<=ed):
		b[r:ed+1] = a[q:ed+1]
	printArray(a)
	printArray(b)

def mergeSort(a, b, st, ed):
	if(st>=ed):
		return
	mid = int((st+ed)/2)

	mergeSort(b, a, st, mid)
	mergeSort(b, a, mid+1, ed)

	merge(b, a, st, ed)

mergeSort(a, b, 0, N-1)
printArray(a)
