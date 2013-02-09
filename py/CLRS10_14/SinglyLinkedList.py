class SinglyLinkedListNode:
	def __init__(self, value):
		self.value = value
		self.nxt = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.length = 0

	def addFirst(self, nextNode):
		if self.head == None:
			self.head = nextNode
		else:
			nextNode.nxt = self.head
			self.head = nextNode
		self.length += 1

	def addLast(self, nextNode):
		if self.head == None:
			self.head = nextNode
		else:
			p = self.head
			while not p.nxt == None:
				p = p.nxt
			p.nxt = nextNode
		self.length += 1

	def deleteFirst(self):
		if self.head != None:
			self.head = self.head.nxt
			self.length -= 1

	def deleteLast(self):
		if self.head != None:
			p = self.head
			if p.nxt == None:
				self.head = None
			else:
				while not p.nxt.nxt == None:
					p = p.nxt
				p.nxt = None
			self.length -= 1

	def delete(self, v):
		if self.head == None:
			return
		if self.head.value == v:
			self.head = self.head.nxt
			self.length -= 1
		else:
			p = self.head
			while not p.nxt.nxt == None:
				if not p.nxt.value == v:
					p = p.nxt

			if p.nxt.nxt == None:
				return
			p.nxt = p.nxt.nxt
			self.length -= 1

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

	def isPalindromeWrapper(self):
		isp, right = self.isPalindrome(self.head, self.length)
		print(isp)

	def isPalindrome(self, head, length):
		if head == None:
			return True, None		

		if length == 1:
			return True, head

		if length == 2:
			isp = head.value == head.nxt.value
			return isp, head.nxt

		isp, right = self.isPalindrome(head.nxt, length-2)
		if not isp:
			return False, right.nxt
		else:
			isp = head.value == right.nxt.value
			return isp, right.nxt

	def swapElements(self):
		if self.head == None or self.head.nxt == None:
			return

		nHead = self.head.nxt
		self.head.nxt = nHead.nxt
		nHead.nxt = self.head
		p = self.head.nxt
		prev = self.head
		if p != None:
			q = p.nxt

		while p != None and q != None:
			prev.nxt = q
			p.nxt = q.nxt
			q.nxt = p
			prev = p
			p = p.nxt
			if p != None:
				q = p.nxt

		self.head = nHead


if __name__ == '__main__':

	import random
	lst = SinglyLinkedList()
	N = 9
	for i in range(0, N):
		lst.addLast(SinglyLinkedListNode(int(random.uniform(0, 4*N))))

	lst.printList()
	lst.reverseList()
	lst.printList()
	lst.reverseListRecursiveWrapper()
	lst.printList()

	lst.swapElements()
	lst.printList()
	
#	lst2 = SinglyLinkedList()
#	for i in range(1,6):
#		lst2.addLast(SinglyLinkedListNode(i))
#	for i in range(4,0,-1):
#		lst2.addLast(SinglyLinkedListNode(i))
#	lst2.addLast(SinglyLinkedListNode(1))
#	lst2.printList()
#	lst2.isPalindromeWrapper()
