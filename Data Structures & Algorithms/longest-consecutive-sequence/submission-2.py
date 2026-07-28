class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        result = 1
    
        nums = set(nums)
    
        for num in nums:
            if num - 1 not in nums:
                current = num
                current_result = 1
                while current + 1 in nums:
                    current += 1
                    current_result += 1
                result = max(result, current_result)
    
        return result
    