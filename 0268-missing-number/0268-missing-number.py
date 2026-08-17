class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        total = n * (n + 1) // 2
        current = sum(nums)

        return total - current