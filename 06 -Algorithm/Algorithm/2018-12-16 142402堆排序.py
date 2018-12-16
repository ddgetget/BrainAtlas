# 堆调整
def ajust(alist, low, high):
	i = low
	tmp = alist[i]
	# 左节点
	j= 2 * i +1
	while j <= high:
		# 选最大子节点
		# 最大子节点和堆顶元素比较
		if j+1 < high and alist[j] < alist[j+1]:
			j += 1
			
		if alist[j] >= tmp:
			alist[i] = alist[j]
			# 沿着破坏的路径走下去
			i= j
			j = 2 * i + 1
		else:
			break
		
		
	alist[i] = tmp
	
# 堆排序
def sort(alist):
	n = len(alist)
	# 1. 无序列表构造标准大顶堆
	for f in range(int(n/2)-1,-1,-1):
		ajust(alist,f,n-1)
	# 2. 堆排序
	for z in range(n-1,-1,-1):
		alist[0],alist[z] = alist[z],alist[0]
		ajust(alist,0,z-1)
		
	return alist
	
if __name__ == "__main__":
	alist = [0,2,6,98,5,23,11,89,100,7]
	print("排序之前:{}".format(alist))
	a = sort(alist)
	print("排序之后:{}".format(a))
	
	