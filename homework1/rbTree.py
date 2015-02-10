class RBtree:

	class RBnode:
    
	    def __init__(self, item):
	        self.value = item
	        self.left = None
	        self.right = None
	        self.parent = None
	        self.color = False

	    def flip_color(self):
	        self.color = not self.color

	def __init__(self):
		self.root = None
		self.size = 0

	def add(self, item):
		if self.root == None:
			self.root = RBtree.RBnode(item)
		else:
			self.go_lower(self.root, item)
		self.size += 1

	def add_left(self, parent, item):
		if parent.left == None:
			parent.left = RBtree.RBnode(item)
			parent.left.parent = parent
			self.fixTree(parent, parent.left)
		else:
			self.go_lower(parent.left, item)

	def add_right(self, parent, item):
		if parent.right == None:
			parent.right = RBtree.RBnode(item)
			parent.right.parent = parent
			self.fixTree(parent, parent.right)
		else:
			self.go_lower(parent.right, item)

	def go_lower(self, parent, item):
		if item < parent.value:
			self.add_left(parent, item)
		elif item > parent.value:
			self.add_right(parent, item)
		else:
			raise ValueError, "Cannot add Duplicate Items"

	def fixTree(self, parent, child):
		pass