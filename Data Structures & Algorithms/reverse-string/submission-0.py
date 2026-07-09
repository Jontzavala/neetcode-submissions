class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) -1
        while left < right:
            old_left = s[left]
            s[left] = s[right]
            s[right] = old_left
            left += 1
            right -= 1