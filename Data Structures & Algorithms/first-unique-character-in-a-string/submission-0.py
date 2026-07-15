class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for j in range(len(s)):
            if s[j] in count and count[s[j]] == 1:
                return j
            else:
                continue
        return -1