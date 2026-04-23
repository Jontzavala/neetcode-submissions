class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 2):
            left = i + 1
            right = len(sorted_nums) - 1
            if i > 0 and sorted_nums[i] == sorted_nums[i -1]:
                continue
            while left < right:
                current_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    output.append([sorted_nums[i],sorted_nums[left],sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left -1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
                    
        return output
