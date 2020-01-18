'''
Python program for basic implementation of Trees
Assumption: unique elements
operations:
Insert
Search
Delete
Print (InOrder traversal)
'''

class Node:
	def __init__(self):
		self.value = None
		self.left_child = None
		self.right_child = None

class BST:
	def __init__(self):
		self.root = None

	def insert(self, root, element):
		'''
		Insert element in Trees
		:element - element to be inserted in Trees
		'''
		node = Node()
		node.value = element
		temp = self.root
		if not self.root:
			self.root = node
		else:
			if element > root.value:
				if not root.right_child:
					root.right_child = node
				else:
					self.insert(root.right_child, element)

			if element < root.value:
				if not root.left_child:
					root.left_child = node
				else:
					self.insert(root.left_child, element)

	def in_order(self, root):
		if root:
			self.in_order(root.left_child)
			print(root.value)
			self.in_order(root.right_child)

	def search(self, root, element):
		if not root:
			print('element not found')
			return False

		if element > root.value:
			self.search(root.right_child, element)

		elif element < root.value:
			self.search(root.left_child,element)

		else:
			print('element search', element)
			return True



if __name__ == '__main__':
	tree = BST()
	tree.insert(tree.root, 2)
	tree.insert(tree.root, 1)
	tree.insert(tree.root, 3)
	tree.insert(tree.root, 7)
	tree.insert(tree.root, 5)
	tree.in_order(tree.root)
	sig = tree.search(tree.root, 9)
	print(sig)







