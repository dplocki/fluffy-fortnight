class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                for c in range(1, n + 1):
                    if a * a + b * b == c * c:
                        result += 1
        return result
