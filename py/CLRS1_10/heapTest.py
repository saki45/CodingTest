from HeapUtil import MaxHeap,PriorityQ 
import random

N = 7
a = []
for i in range(0, N):
	a.append(int(random.uniform(0, 8*N)))

def printList(a):
	for i in a:
		print(i, end=' ')
	print()

printList(a)

#mh = MaxHeap(a)
#mh.printHeap()
#mh.makeHeap()
#mh.printHeap()

pr = PriorityQ(a)

#pr.printQueue()
pr.printHeap()
print(pr.extractMax())
pr.printHeap()
pr.addKey(60)
pr.printHeap()
