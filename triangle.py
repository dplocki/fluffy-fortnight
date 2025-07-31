class Solution:
    MAX_VALUE = 10**4

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = { 0: triangle[0][0] }

        for line in triangle[1:]:
            current_result = {}
            for index, number in enumerate(line):
                current_result[index] = min(
                    result.get(index - 1, Solution.MAX_VALUE),
                    result.get(index, Solution.MAX_VALUE)
                ) + number

            result = current_result

        return min(result.values())
