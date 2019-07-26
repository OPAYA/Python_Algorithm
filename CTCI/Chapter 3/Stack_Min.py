
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
  
        #min_val = self.getMin() if self.stack else x
        if self.stack:
            min_val = self.getMin()
        else:
            min_val = x
        self.stack.append((x, min(min_val, x)))
        print(self.stack[-1])
#        print(self.stack[-1])

    def pop(self):
        """
        :rtype: None
        """

        return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:

obj = MinStack()
obj.push(3)
obj.push(2)
obj.push(4)
obj.push(1)


param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)