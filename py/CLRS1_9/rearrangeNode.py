from ListNodeDef import ListNode

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.nextNode = n2
n2.nextNode = n3
n3.nextNode = n4

n1.printList()

def rearrangeNode(head):
	pa = head
	pb = head.nextNode

	while pb.nextNode != None:
		pb = pb.nextNode.nextNode
		pa = pa.nextNode

	pb = pa.nextNode
	pa = head

	while pb.nextNode != None:
		ta = pa.nextNode
		tb = pb.nextNode
		pa.nextNode = pb
		pb.nextNode = ta
		pa = ta
		pb = tb

	pa.nextNode = pb

rearrangeNode(n1)
n1.printList()
