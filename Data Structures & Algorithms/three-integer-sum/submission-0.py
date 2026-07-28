class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != j and i != k and j != k:
                        current = nums[i] + nums[j] + nums[k]
                        current_vals = [nums[i], nums[j], nums[k]]
                        current_vals.sort()
                        if current == 0 and current_vals not in res:
                            res.append(current_vals)
        return res