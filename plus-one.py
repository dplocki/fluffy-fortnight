class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        move = 1
        for digit in reversed(digits):
            if move == 0 and digit < 9:
                result.append(digit + move)
            else:
                tmp = digit + move
                result.append(tmp % 10)
                move = tmp // 10

        if move > 0:
            result.append(move)

        return list(reversed(result))
