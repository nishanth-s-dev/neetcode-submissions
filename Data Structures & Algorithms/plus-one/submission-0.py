class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for num in digits:
            n *= 10
            n += num
            
        n += 1
        return list(str(n))