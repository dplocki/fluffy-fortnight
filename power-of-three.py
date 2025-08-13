class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        # The maxium in given n-range: 3 ** 19
        return 1162261467 % n == 0
