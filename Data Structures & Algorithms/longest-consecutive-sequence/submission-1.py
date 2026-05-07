class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        my_set = set(nums)
        for num in my_set:
            current_streak = 0
            if num - 1 not in my_set:
                while num in my_set:
                    current_streak += 1
                    num = num + 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak
