from collections import Counter

class Solution:
    def get_most_frequent_char_count(self, string):
        count = 0
        for i in range(len(string)):
            current_count = 0
            for j in range(len(string)):
                if string[i] == string[j]:
                    current_count += 1
            count = max(current_count, count)
        return count
    
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                substring = s[i:j]
                most_frequenct_char_count = self.get_most_frequent_char_count(substring)
                steps_needed = len(substring) - most_frequenct_char_count
                if steps_needed <= k:
                    res = max(res, len(substring))
        return res

