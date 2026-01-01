class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        move = 1

        for digit in reversed(digits):
            new_digit = digit + move
            if new_digit == 10:
                new_digit = 0
                move = 1
            else:
                move = 0

            result.append(new_digit)
        
        if move != 0:
            result.append(move)
        
        return result[::-1]
