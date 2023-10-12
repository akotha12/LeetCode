class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.counter = 0
        self.len = 1
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.history = self.history[0:self.counter + 1]
        self.history.append(url)
        self.counter += 1
        self.len = len(self.history)
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.counter -= steps
        if self.counter < 0:
            self.counter = 0
        return self.history[self.counter]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.counter += steps
        if self.counter >= self.len:
            self.counter = self.len - 1
        return self.history[self.counter]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)