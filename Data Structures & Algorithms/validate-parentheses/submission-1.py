class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {'{' : '}', '(' : ')', '[' : ']'}
        for char in s:
            if self.is_open_parentheses(char):
                stack.append(char)
            if self.is_close_parentheses(char):
                if not stack:
                    return False
                current = stack.pop()
                if parentheses_map[current] != char:
                    return False
        
        return len(stack) == 0
    
    def is_open_parentheses(self, char):
        return char in '{(['
    
    def is_close_parentheses(self, char):
        return char in '})]'