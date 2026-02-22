class Solution:
    def binaryGap(self, n: int) -> int:
        prev_index = inf
        result = 0
        index = 0

        while n != 0:
            bit = n & 1
            if bit == 1:
                result = max(result, index - prev_index)
                prev_index = index

            n >>= 1
            index += 1

        return result
