class Solution:
    def countTriples(self, n: int) -> int:
        result = 0
        sqare_c = set(c * c for c in range(1, n + 1))

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                sum_a2_b2 = a * a + b * b
                if sum_a2_b2 in sqare_c:
                    result += 1

        return result
