class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = 999999999
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
                continue
            elif maxProfit < price - minPrice:
                maxProfit = price - minPrice
        return maxProfit