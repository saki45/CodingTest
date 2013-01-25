class SinglyLinkedListNode:
	def __init__(self, value):
		self.value = value
		self.nxt = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def addFirst(self, nextNode):
		if self.head == None:
			self.head = nextNode
		else:
			nextNode.nxt = self.head
			self.head = nextNode

	def addLast(self, nextNode):
		if self.head == None:
			self.head = nextNode
		else:
			p = self.head
			while not p.nxt == None:
				p = p.nxt
			p.nxt = nextNode

	def deleteFirst(self):
		if not self.head == None:
			self.head = self.head.nxt

	def deleteLast(self):
		if not self.head == None:
			p = self.head
			if p.nxt == None:
				self.head = None
			else:
				while not p.nxt.nxt == None:
					p = p.nxt
				p.nxt = None

	def delete(self, v):
		if self.head == None:
			return
		if self.head.value == v:
			self.head = self.head.nxt
		else:
			p = self.head
			while not p.nxt.nxt == None:
				if not p.nxt.value == v:
					p = p.nxt

			if p.nxt.nxt == None:
				return
			p.nxt = p.nxt.nxt

	def printList(self):
		if self.head == None:
			print('None')

		p = self.head
		while not p.nxt == None:
			print(p.value, end='->')
			p = p.nxt
		print(p.value)

	def reverseList(self):
		if self.head == None or self.head.nxt == None:
			return

		p, q, r = self.head, self.head.nxt, self.head.nxt.nxt
		
		while not q == None:
			q.nxt = p
			p = q
			q = r
			if not r == None:
				r = r.nxt
		self.head.nxt = None
		self.head = p

	def reverseListRecursive(self, head):
		if head.nxt == None:
			return head, head
		else:
			nh, nt = self.reverseListRecursive(head.nxt)
			nt.nxt = head
			head.nxt = None
			return nh, head

	def reverseListRecursiveWrapper(self):
		self.head, tmp = self.reverseListRecursive(self.head)


if __name__ == '__main__':

	import random
	lst = SinglyLinkedList()
	N = 8
	for i in range(0, N):
		lst.addLast(SinglyLinkedListNode(int(random.uniform(0, 4*N))))

	lst.printList()
	lst.reverseList()
	lst.printList()
	lst.reverseListRecursiveWrapper()
	lst.printList()
