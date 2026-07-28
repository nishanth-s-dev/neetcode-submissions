class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        res = 1
        current = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            if diff > 1:
                res = max(res, current)
                current = 1
            elif diff == 0:
                continue
            else:
                current += 1

        return max(res, current)