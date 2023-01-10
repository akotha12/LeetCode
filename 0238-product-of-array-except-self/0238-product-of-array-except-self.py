class Solution(object):
    def productExceptSelf(self, nums):
        total = 1
        numZero = 0
        total2 = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                numZero += 1
            else:
                total2 *= nums[i]
            total *= nums[i]
            print(total)
            print(total2)
        for i in range(len(nums)):
            if (nums[i] == 0 and numZero < 2):
                nums[i] = 1
                nums[i] = total2
                print('n = ', nums[i])
            elif (nums[i] == 0 and numZero > 1):
                nums[i] = 0
            else:
                nums[i] = total / nums[i]
                print(nums[i])
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        