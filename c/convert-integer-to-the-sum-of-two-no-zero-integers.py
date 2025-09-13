class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for first in range(1, n // 2 + 1):
            second = n - first
            if str(first).count('0') > 0 or str(second).count('0') > 0:
                continue

            return [first, second]
