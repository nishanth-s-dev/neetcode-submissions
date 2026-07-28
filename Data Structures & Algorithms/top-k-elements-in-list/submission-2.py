class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = sorted(Counter(nums).items(), key=lambda field: field[1], reverse=True)

        res = []
        for key, value in frequency:
            if k <= 0:
                break
            res.append(key)
            k -= 1

        return res