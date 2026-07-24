class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0
        max_output = 0
        for right in range(len(s)):
            if s[right] in seen:
                seen[s[right]] += 1
            else:
                seen[s[right]] = 1
            while (right - left + 1) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1
            max_output = max(max_output, right - left + 1)
        return max_output

