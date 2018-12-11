
class BaseNode(object): 
	"""单向链表的结点"""
	def __init__(self,item):
		# item 存放数据元素
		self.item = item
		# next 是下一个结点的地址
		self.next = None

	def add(self,item):
		# 1. 实例化新节点
		node = BaseNode(item)
		# 2. 找位置
		# 3. 修改属性
		node.next = self.__head
		self.__head=node

	# 尾部增加
	def append(self,item):
		pass

	# 指定位置增加
	def insert(self,pos,item):
		pass
	
if __name__  == "__main__":
	print("ok")
	node = BaseNode(100) 
	print(node.item)
	print(node.next)

	