class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        max_output = 0
        left = 0
        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[right])
            max_output = max((right - left) + 1, max_output)
        return max_output