class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_hash = {}
        if len(ransomNote) > len(magazine):
            return False
        for i in magazine:
            if i in my_hash:
                my_hash[i] += 1
            else:
                my_hash[i] = 1
        for m in ransomNote:
            if m in my_hash:
                my_hash[m] -= 1
                if my_hash[m] == 0:
                    del my_hash[m]
            else:
                return False
        return True