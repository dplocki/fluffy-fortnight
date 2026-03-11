class Solution:
    def minOperations(self, s: str, k: int) -> int:
        zeros = s.count('0')
        length = len(s)
        if zeros == 0:
            return 0

        if length == k:
            return 1 if zeros == length else -1

        base = length - k
        odd = max(
            (zeros + k - 1) // k,
            (length - zeros + base - 1) // base
        )

        if odd % 2 == 0:
            odd += 1

        even = max(
            (zeros + k - 1) // k,
            (zeros + base - 1) // base
        )

        if even % 2 == 1:
            even += 1

        result = float('inf')
        if k % 2 == zeros % 2:
            result = min(result, odd)

        if zeros % 2 == 0:
            result = min(result, even)

        return -1 if result == float('inf') else result
