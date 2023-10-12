class HitCounter(object):

    def __init__(self):
        self.hits = []

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        self.hits.append(timestamp)
        self.removeOldHits(timestamp)

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        self.removeOldHits(timestamp)
        return len(self.hits)
    
    def removeOldHits(self, timestamp):
        while len(self.hits) >= 1 and self.hits[0] <= timestamp - 300:
            self.hits.remove(self.hits[0])
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)