class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_output = 0
        my_hash = {}
        for right in range(len(s)):
            if s[right] in my_hash:
                my_hash[s[right]] += 1
            else:
                my_hash[s[right]] = 1
            while (right - left + 1) - max(my_hash.values()) > k:
                my_hash[s[left]] -= 1
                left += 1
            max_output = max((right - left + 1), max_output)
        return max_output