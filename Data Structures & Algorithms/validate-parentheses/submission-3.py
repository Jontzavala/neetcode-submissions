class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for i in s:
            if i in pairs:
                if not stack:
                    return False
                opening = stack[-1]
                if pairs[i] != opening:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False