class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for current_num in nums2:
            while stack and current_num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = current_num
            stack.append(current_num)
        while stack:
            number = stack.pop()
            next_greater[number] = -1
        output = []
        for num in nums1:
            output.append(next_greater[num])
        return output




