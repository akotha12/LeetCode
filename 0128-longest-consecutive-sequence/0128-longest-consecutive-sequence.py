class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
            
        """
        :type nums: List[int]
        :rtype: int
        """
        