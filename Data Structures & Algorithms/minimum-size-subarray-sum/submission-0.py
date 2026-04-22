class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = 0
        subarray_sum = 0
        for right in range(len(nums)):
            subarray_sum += nums[right]
            while subarray_sum >= target:
                min_length = min(right - left + 1, min_length)
                subarray_sum -= nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        else:
            return min_length