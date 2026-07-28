class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            check_set = set()
            count = 0
            for j in range(i, len(s)):
                if s[j] not in check_set:
                    count += 1
                    check_set.add(s[j])
                else:
                    break
            res = max(res, count)
        return res