class Solution:
    def countTriples(self, n: int) -> int:
        sqare_c = set(c * c for c in range(1, n + 1))

        return sum(1
            for a in range(1, n + 1)
            for b in range(1, n + 1)
            if a * a + b * b in sqare_c)
