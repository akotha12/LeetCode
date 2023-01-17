class MinStack(object):

    def __init__(self):
        self.values = []        

    def push(self, val):
        if self.values:
            self.values.append((val, min(val, self.values[-1][1])))
        else:
            self.values.append((val, val))
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        self.values.pop()
        """
        :rtype: None
        """
        

    def top(self):
        return self.values[-1][0]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.values[-1][1]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()