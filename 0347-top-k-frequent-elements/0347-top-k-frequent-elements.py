class Solution(object):
    def topKFrequent(self, nums, k):
        myMap = {}
        max = 0
        output = []
        for i in range(len(nums)):
            if myMap.has_key(nums[i]):
                myMap[nums[i]] += 1
            else:
                myMap[nums[i]] = 1
        frequency = sorted(myMap.items(), key=lambda x:x[1])
        tmp = frequency[-k:]
        print(tmp);
        for value in tmp:
            output.append(int(value[0]))
        return output
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        