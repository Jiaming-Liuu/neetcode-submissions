from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [];
        pairs = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char not in pairs:
                stack.append(char)
            elif not stack or stack[-1] != pairs[char]:
                return False
            else:
                stack.pop()
        return not stack