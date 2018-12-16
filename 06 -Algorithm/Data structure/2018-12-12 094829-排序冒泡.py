# 冒泡原理

# 1. 元素比较：相邻元素两两比较，打的元素和后面的元素比较
# 2. 排序内容：比较循环，n-1次元素比较将最大的额元素放到合适的位置
# 3. 整体内容：外部冒泡循环，经过n-1次冒泡排序，最终形成一个从小到达的有序序列
def bubble_sort(alist):
	n = len(alist)
	# 循环的范围
	for j in range(n-1,0,-1):
		# 开始比较前，定义计数器count的初始值为0
		count = 0
		# 内层的数据比较循环范围
		for i in range(j):
			if alist[i] > alist[i+1]:
				alist[i],alist[i+1]=alist[i+1],alist[i]
				# 数据替换完毕,计数器+1
				count+=1
		
		# 如果计数器的值为0，表示没有发生任何替换，那么久就退出当前循环
		if count == 0:
			break
			
if __name__ == "__main__":
	li=[]
	for i in range(1000):
		num = random.randint(100)
		li.append(i)
	# li = [45,78,69,453,21,96,785,652,42]
	print(li)
	bubble_sort(li)
	print(li)