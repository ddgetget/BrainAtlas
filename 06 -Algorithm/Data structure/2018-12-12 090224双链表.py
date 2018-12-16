
class BaseNode(object):
	def __init__(self,item):
		self.item=item
		self.next=None
		self.pre = None
class DoubleLinkNode(object):
	def __init__(self,node=None):
			self.__head=node
	
	# is_empty()
	def is_empty(self):
		pass
	# 链表元素数量：length()		
	# 链表内容查看：travel()	
	# 链表内容搜索: search(item)

	# 插头增: add(item)		
	# 内容删除: remove(item) 
	# 插尾增: append(item)
	# 指定位置增: insert(pos,item)

	
if __name__=="__main__":
	node = BaseNode(100)
	print(node.item)
	print(node.pre)
	print(node.next)