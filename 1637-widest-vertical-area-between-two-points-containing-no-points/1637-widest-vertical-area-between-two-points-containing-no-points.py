class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[0])
        output = 0
        for i in range(1, len(points)):
            output = max(output, points[i][0] - points[i - 1][0])
            
        return output