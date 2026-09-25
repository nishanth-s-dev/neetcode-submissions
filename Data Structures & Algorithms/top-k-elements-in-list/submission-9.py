class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = dict(sorted(counter.items(), key=lambda item: -item[1]))
        res = list(sorted_counter.keys())[:k]
        return res
        