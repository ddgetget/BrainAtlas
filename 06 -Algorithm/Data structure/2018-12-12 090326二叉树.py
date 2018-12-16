class BaseNode(object):
	def __init__(self, item):
		self.lsub=None
		self.item-item
		self.rsub=None
		
		
class Tree(object):
	def __init__(self, node=None):
		self.root = node
		
	def add(self, item):
		# 1. 实例化树
		node = BaseNode(item)
		
		if self.root == None:
			self.root = node
		else:
			pass

if __name__ == "__main__":
	print("ok")