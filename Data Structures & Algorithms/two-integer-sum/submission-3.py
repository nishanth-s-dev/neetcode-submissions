class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in tracker:
                return [tracker[diff], index]
            else:
                tracker[num] = index
        return []


"""
{ 4: 0 }

7 - 3 = 4
7 - 4 = 

"""