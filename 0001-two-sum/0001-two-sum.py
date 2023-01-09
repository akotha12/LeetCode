class Solution(object):
    def twoSum(self, nums, target):
        myMap = {};
        for i in range(len(nums)):
            if nums[i] in myMap:
                return [myMap[nums[i]], i]
            else:
                myMap[target - nums[i]] = i
        return 0;
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        