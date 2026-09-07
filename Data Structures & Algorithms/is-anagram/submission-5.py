class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for j in t:
            if j in hashmap:
                hashmap[j] -= 1
                if hashmap[j] == 0:
                    del hashmap[j]
            else:
                return False
        return True