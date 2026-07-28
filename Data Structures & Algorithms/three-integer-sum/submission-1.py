class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                for k in range(len(numbers)):
                    if i != j and i != k and j != k:
                        current_sum = numbers[i] + numbers[j] + numbers[k]
                        if current_sum == 0:
                            current_vals = [numbers[i], numbers[j], numbers[k]]
                            current_vals.sort()
                            if current_vals not in res:
                                res.append(current_vals)
        return res