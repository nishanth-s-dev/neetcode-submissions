class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        has_duplicate = [number != nums[index + 1] for index, number in enumerate(nums[:-1])]
        return not all(has_duplicate)