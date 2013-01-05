class MaxHeap:
	def __init__(self, arr):
		self.a = arr
		self.size = len(self.a)
	
	def heapify(self, i):
		root, largest= i, -1
		while not largest==root:
			largest = root
			l, r = 2*root+1, 2*root+2
			if l < self.size and self.a[l]>self.a[largest]:
				largest = l
			if r < self.size and self.a[r]>self.a[largest]:
				largest = r

			if not largest == root:
				tmp = self.a[root]
				self.a[root] = self.a[largest]
				self.a[largest] = tmp
				root = largest
				largest = -1

	def makeHeap(self):
		for i in range(int(self.size/2)-1,-1,-1):
			self.heapify(i)

	def printHeap(self):
		p, l = 0, 0
		while p < self.size:
			print(self.a[p], end=' ')
			if p == l:
				print()
				l = 2*p+2
			p += 1
		print()

class PriorityQ(MaxHeap):
	def __init__(self, arr):
		MaxHeap.__init__(self, arr)
		self.makeHeap()

	def printQueue(self):
		for i in self.a:
			print(i, end=' ')
		print()

	def getMax(self):
		return self.a[0]

	def extractMax(self):
		curMax = self.a[0]
		self.a[0] = self.a.pop()
		self.heapify(0)
		self.size -= 1
		return curMax

	def increaseKey(self, i, key):
		if key < self.a[i]:
			return

		root, parent = i, int((i-1)/2)
		while parent < root and key > self.a[parent]:
			self.a[root] = self.a[parent]
			root = parent
			parent = int((root-1)/2)
		self.a[root] = key

	def addKey(self, key):
		self.a.append(key)
		self.size += 1
		self.increaseKey(self.size-1, key)
