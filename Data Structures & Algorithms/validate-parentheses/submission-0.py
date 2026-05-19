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
                if pairs[i] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True