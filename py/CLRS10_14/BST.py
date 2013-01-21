class BinarySearchTreeNode:
	def __init__(self, key = 0):
		self.key = key
		self.ltree = None
		self.rtree = None

class BinarySearchTree:
	def __init__(self, root = None):
		self.root = root;

	########## Add / Delete Nodes #########

	def add(self, node):
		p = self.root
		while p != None:
			if node.key >= p.key:
				p = p.rtree
			else:
				p = p.ltree
		p = node

	########### Tree Traversal (Recursive) ###########

	def preorderRW(self):
		preorderR(self.root)

	def preorderR(self, node):
		if node == None:
			return

		print(node.key, end = ' ')
		preorderR(node.ltree)
		preorderR(node.rtree)

	def inorderRW(self):
		inorderR(self.root)

	def inorderR(self, node):
		if node == None:
			return

		inorderR(node.ltree)
		print(node.key, end = ' ')
		inorderR(node.rtree)

	def postorderRW(self):
		postorderR(self.root)

	def postorderR(self, node):
		if node == None:
			return

		postorderR(node.ltree)
		postorderR(node.rtree)
		print(node.key, end = ' ')
