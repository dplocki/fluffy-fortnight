MOD = 10**9 + 7

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1

        dp_up = [1] * m
        dp_down = [1] * m
        for _ in range(n - 1):
            sum_up = list(accumulate(dp_up, initial=0))
            sum_down = list(accumulate(dp_down, initial=0))

            dp_up = [x % MOD for x in sum_down[:-1]]

            last_up = sum_up[-1]
            dp_down = [(last_up - x) % MOD for x in sum_up[1:]]

        return (sum(dp_up) + sum(dp_down)) % MOD
