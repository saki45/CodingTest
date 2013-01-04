class ListNode:
	def __init__(self,value=0,nextNode=None):
		self.data = value
		self.nextNode = nextNode
	def printList(self):
		print self.data
		if(self.nextNode != None):
			self.nextNode.printList()

