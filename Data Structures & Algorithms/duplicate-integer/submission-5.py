class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for index, number in enumerate(nums[:-1]):
            if number == nums[index + 1]: return True
        
        return False