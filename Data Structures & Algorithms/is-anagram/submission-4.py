class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in s_hash:
                s_hash[i] += 1
            else:
                s_hash[i] = 1
        for j in t:
            if j in s_hash:
                s_hash[j] -= 1
                if s_hash[j] == 0:
                    del s_hash[j]
            else:
                return False
        return True

