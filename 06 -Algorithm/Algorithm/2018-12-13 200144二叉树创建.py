class Node(object):
	def __init__(self, item):
		self.elem = item
		self.lchild = None
		self.rchild = None
	
class Tree(object):
	def __init__(self):
		self.root = None
	
	def add(self,item):
		node = Node(item)
		if self.root is None:
			self.root = node
			return
			
		queue = [self.root]
		
		while queue:
			cur_node = queue.pop(0)
			if cur_node.lchild is None:
				cur_node.lchild = node
				return
			else:
				queue.append(cur_node.lchild)
			
			if cur_node.rchild is None:
				cur_node.rchild = node
				return
			else:
				queue.append(cur_node.rchild)
		
	
	def breadth_travel(self):
		"""广度遍历"""
		
		if self.root is None:
			return
		
		queue = [self.root]
		
		while queue:
			cur_node = queue.pop(0)
			
			print(cur_node.elem, end=" ")
			
			if cur_node.lchild is not None:
				queue.append(cur_node.lchild)
				
			if cur_node.rchild is not None:
				queue.append(cur_node.rchild)
				
	def preorder(self, node):
		"""先序"""
		if node is None:
			return
			
		print(node.elem,end=" ")
		self.preorder(node.lchild)
		self.preorder(node.rchild)
	
	def inorder(self, node):
		"""先序"""
		if node is None:
			return
			
		self.inorder(node.lchild)
		print(node.elem,end=" ")
		self.inorder(node.rchild)
	
	def posorder(self, node):
		"""先序"""
		if node is None:
			return
			
		self.posorder(node.lchild)
		self.posorder(node.rchild)
		print(node.elem,end=" ")
		
			
if __name__ == "__main__":
	tree=Tree()
	tree.add(3)
	tree.add(10)
	tree.add(24)
	tree.add(1024)
	tree.add(23)
	# 广度遍历
	tree.breadth_travel()
	print("")
	# 先序遍历
	tree.preorder(tree.root)
	print("")
	tree.inorder(tree.root)
	print("")
	tree.posorder(tree.root)