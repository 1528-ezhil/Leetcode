class Solution(object):
    def findLengthOfLCIS(self, nums):

        left = 0
        max_length = 1

        for right in range(1, len(nums)):

            if nums[right] <= nums[right - 1]:
                left = right

            max_length = max(max_length, right - left + 1)

        return max_length