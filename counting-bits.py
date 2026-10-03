class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0]

        for index in range(1, n + 1):
            result.append(result[index >> 1] + (index & 1))

        return result
