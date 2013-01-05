from QuickSort import quickSort, partition
import random

a = []
N = 12
for i in range(0, N):
	a.append(int(random.uniform(0, 8*N)))

def printList(a):
	for i in a:
		print(i, end = ' ')
	print()

printList(a)

quickSort(a, 0, N-1)
printList(a)
