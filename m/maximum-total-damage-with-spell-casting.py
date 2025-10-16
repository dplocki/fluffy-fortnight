class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        dp = {}
        chains = {}
        prev = -3

        for index, p in enumerate(power):
            if index > 0 and power[index - 1] == p:
                dp[p] += p
                continue

            t = prev
            while t >= p - 2:
                t = chains[t]

            result = dp.get(t, 0)
            s = t
            while s >= t - 2 and s > -1:
                result = max(result, dp.get(s, 0))
                s = chains[s]
                
            dp[p] = result + p
            chains[p] = prev
            prev = p

        return max(
            dp.get(power[-1] - i, 0) 
            for i in range(3))
