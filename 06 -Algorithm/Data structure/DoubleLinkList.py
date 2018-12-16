class BaseNode(object):
    def __init__(self, item):
        self.pre = None
        self.item = item
        self.next = None


class DoubleLinkList(object):
    # 定义操作的基本属性
    def __init__(self, node=None):
        # 确定当前链表的
        self.__head = node

    def is_empty(self):
        # 判断是否为空
        pass

    # 头部增加
    def add(self, item):
        # 1. 实例化节点
        node = BaseNode(item)
        # 2. 找位置
        # 3. 改属性
        node.next = node
        self.__head = node
        if node.next:
            node.next.pre = node

    # 尾部增加
    def append(self, item):

        if self.id_empty():
            return

    def id_empty(self):
        pass

    def remove(self,item):
        # 准备工作
        pass


if __name__ == "__main__":
    pass
