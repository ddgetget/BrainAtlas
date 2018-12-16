class BaseNode(object):
	""""""
	def __init__(self,item):
		self.item=item
		self.next=None

class SingleLinkList(object):
		def __init__(self,node=None):
			self.__head=node
	# 链表是否为空：is_empty()	
	# 插头增: add(item)	
	# 内容删除: remove(item)
	# 链表元素数量：length()	
	# 插尾增: append(item) 
	# 链表内容查看：travel()	
	# 指定位置增: insert(pos,item) 
	# 链表内容搜索: search(item)

if __name__=="__main__":
	node = BaseNode(100)
	print(node.item)
	print(node.next)