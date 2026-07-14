class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for j in t:
            if j in count:
                count[j] -= 1
                if count[j] == 0:
                    del count[j]
            else:
                return False
        if count:
            return False
        else:
            return True