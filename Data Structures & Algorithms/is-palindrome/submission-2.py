class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char.lower() for char in s if self.is_alpha_num(char.lower())])
        l, r = 0, len(s) - 1

        while (l < r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
    
    def is_alpha_num(self, char):
        return ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')
