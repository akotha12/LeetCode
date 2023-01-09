class Solution(object):
    def containsDuplicate(self, nums):
        myset = set(nums)
        output = False
        if len(myset) != len(nums):
            output = True
        return output
        """
        :type nums: List[int]
        :rtype: bool
        """