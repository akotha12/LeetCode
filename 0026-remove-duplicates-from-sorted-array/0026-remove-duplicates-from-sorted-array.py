class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curNum= nums[0]
        count = 1
        for i in range(len(nums)):
            if nums[i] != curNum:
                nums[count] = nums[i]
                count += 1
                curNum = nums[i]
        return count
        