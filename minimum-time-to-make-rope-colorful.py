class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        group = [neededTime[0]]
        prev = colors[0]

        for index, letter in enumerate(colors[1:], 1):
            if letter != prev:
                result += sum(group) - max(group)
                group = []

            group.append(neededTime[index])
            prev = letter

        result += sum(group) - max(group)
        return result
