from QuickSort import quickSort, partition, quickSortE, partitionE
import random

a = []
b = []
N = 16
for i in range(0, N):
	a.append(int(random.uniform(0, 8*N)))
	b.append(int(random.uniform(0, 1*N)))

def printList(a):
	for i in a:
		print(i, end = ' ')
	print()

printList(a)
quickSort(a, 0, N-1)
printList(a)

#printList(b)
#quickSortE(b, 0, N-1)
#printList(b)
