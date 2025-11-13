class Solution:
    def maxOperations(self, s: str) -> int:
        result = 0
        encounter_ones = 0
        for index, digit in enumerate(s):
            if digit == '1':
                encounter_ones += 1
            elif index > 0 and s[index - 1] == '1':
                result += encounter_ones

        return result
