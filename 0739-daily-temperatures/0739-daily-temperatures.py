class Solution(object):
    def dailyTemperatures(self, temperatures):
        myStack = []
        output = [0] * len(temperatures)
        myStack.append((temperatures[0], 0))
        for i in range(len(temperatures)):
            while myStack and temperatures[i] > myStack[-1][0]:
                output[myStack[-1][1]] = i - myStack[-1][1]
                myStack.pop()
            myStack.append((temperatures[i], i))
        return output
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        