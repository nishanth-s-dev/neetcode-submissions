class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {"}" : "{", ")" : "(", "]": "["}

        for char in s:
            if char not in parentheses_map:
                stack.append(char)
            else:
                if not stack or stack[-1] != parentheses_map[char]:
                    return False
                stack.pop()

        return not stack