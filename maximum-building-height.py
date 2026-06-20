class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        restrictions_len = len(restrictions)
        for index in range(1, restrictions_len):
            restrictions[index][1] = min(restrictions[index][1], restrictions[index - 1][1] + restrictions[index][0] - restrictions[index - 1][0])

        for index in range(restrictions_len - 2, 0, -1):
            restrictions[index][1] = min(restrictions[index][1], restrictions[index + 1][1] + (restrictions[index + 1][0] - restrictions[index][0]))

        return max(
            ((restrictions[index + 1][0] - restrictions[index][0]) + restrictions[index][1] + restrictions[index + 1][1]) // 2
            for index in range(restrictions_len - 1)
        )
