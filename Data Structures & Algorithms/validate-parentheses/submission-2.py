class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {"}" : "{", ")" : "(", "]": "["}

        for char in s:
            if char not in parentheses_map:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                current = stack.pop()
                if parentheses_map[char] != current:
                    return False

        return len(stack) == 0
