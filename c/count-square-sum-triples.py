class Solution:
    def countTriples(self, n: int) -> int:
        sqare_c = set(c * c for c in range(1, n + 1))

        return sum(2
            for a, b in combinations(range(1, n + 1), 2)
            if a * a + b * b in sqare_c)
