class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, result = [], [0] * len(temperatures)

        for index, temperatur in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperatur:
                previous_index = stack.pop()
                result[previous_index] = index - previous_index
        
            stack.append(index)

        return result
