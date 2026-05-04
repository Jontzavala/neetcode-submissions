class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            current_index = i
            while stack and current_temp > stack[-1][1]:
                prev_index,prev_temp = stack.pop()
                output[prev_index] = current_index - prev_index
            stack.append((current_index,current_temp))
        return output