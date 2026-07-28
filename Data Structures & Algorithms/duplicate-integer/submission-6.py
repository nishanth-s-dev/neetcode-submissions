class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for number in nums:
            if number in d: return True
            d.add(number)
        
        return False