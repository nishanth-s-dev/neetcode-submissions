class Solution:
    def maxArea(self, nums: List[int]) -> int:
        res = float("-inf")
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                res = max(min(nums[i], nums[j]) * (j - i), res)
        return res
