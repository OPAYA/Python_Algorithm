class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = []
        self.minimum = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.minimum.append(min(self.head, x))
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """
        :rtype: None
        """

        ret_data = self.head.data

        self.head = self.head.next

        return ret_data

    def top(self):
        """
        :rtype: int
        """
        return self.head

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()