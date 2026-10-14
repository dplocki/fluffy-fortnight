class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ''

        number_of_9, rest = divmod(sum, 9)
        result = '9' * number_of_9
        if rest > 0:
            result += str(rest)

        result += '0' * (num - len(result))
        return result
