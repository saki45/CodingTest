def partition1(arr):
	# from head and tail, move to middle
	a = arr.copy()
	p, q, r = 0, 0, len(a)-1
	while q < r:
		while a[p] == 0:
			p += 1
		while a[r] == 2:
			r -= 1
		q = p
		while a[q] != 2:
			if a[q] == 1:
				q += 1
			else:
				a[q], a[p] = a[p], a[q]
				q += 1
				p += 1 
		if q < r:
			a[q], a[r] = a[r], a[q]

	print(a)

def partition2(arr):
	# all from head
	a = arr.copy()
	p, q, r = 0, 0, 0
	while r < len(a):
		if a[r] == 2:
			r += 1
		elif a[r] == 1:
			a[r], a[q] = a[q], a[r]
			q += 1
			r += 1
		else:
			tmp = a[r]
			a[r] = a[q]
			a[q] = a[p]
			a[p] = tmp
			r += 1
			q += 1
			p += 1
	print(a)

if __name__ == '__main__':
	import random
	N = 20
	arr = [int(random.uniform(0, 2.9)) for i in range(N)]
	print(arr)

	partition1(arr)
	partition2(arr)
