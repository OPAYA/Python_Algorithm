class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None
        
class MyQueue(object):

    def __init__(self):
        self.head = None
        self.tail = None
        """
        Initialize your data structure here.
        """
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        new_data = Node(x)
        if self.head is None:
            self.head = new_data
            self.tail = self.head
        else:
            self.tail.next = new_data
            self.tail = new_data
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail is None
        return data
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.head.data

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.head == None
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()