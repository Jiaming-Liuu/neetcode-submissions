from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque();
        for i in range(len(s)):
            if s[i] in ['{', '[', '(']:
                stack.append(s[i])
            elif (stack[-1] == '{' and s[i] == '}') or (stack[-1] == '[' and s[i] == ']') or (stack[-1] == '(' and s[i] == ')'):
                stack.pop()
            else:
                return False;
        return True;