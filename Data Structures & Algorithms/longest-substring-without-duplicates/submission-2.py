class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        check_set = set()
        left = 0
        for right in range(len(s)):
            while s[right] in check_set:
                check_set.remove(s[left])
                left += 1
            check_set.add(s[right])
            res = max(res, right - left + 1)

        return res