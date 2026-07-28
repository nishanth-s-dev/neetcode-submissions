class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(list(set(nums)))
        nums.sort()
    
        result = 1
        current_result = 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 1:
                current_result += 1
            else:
                result = max(result, current_result)
                current_result = 1
    
        result = max(current_result, result)
    
        return result
