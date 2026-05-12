class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextgreater_hash = {}
        answer = []
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                nextgreater_hash[prev] = num
            stack.append(num)
        for num in nums1:
            answer.append(nextgreater_hash.get(num, -1))
        return answer
            