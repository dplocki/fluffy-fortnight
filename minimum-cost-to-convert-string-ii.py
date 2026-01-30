class Solution:
    INFINITY = float('inf')

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        nodes = set(original) | set(changed)
        costs = {}
        for node in nodes:
            if node not in costs:
                costs[node] = {}
                
            if node not in costs[node]:
                costs[node][node] = 0

        lengths = set()
        for a, b, c in zip(original, changed, cost):
            costs[a][b] = min(c, costs[a].get(b, Solution.INFINITY))
            lengths.add(len(a))

        for b in nodes:
            for a in nodes:
                for c in nodes:
                    costs[a][c] = min(costs[a].get(b, Solution.INFINITY) + costs[b].get(c, Solution.INFINITY), costs[a].get(c, Solution.INFINITY))

        n = len(source)        
        dp = { i:Solution.INFINITY for i in range(n + 1) }
        dp[0] = 0

        for start in range(n):
            if dp[start] == Solution.INFINITY:
                continue

            if source[start] == target[start]:
                dp[start + 1] = min(dp[start + 1], dp[start])

            for length in lengths:
                end = start + length
                if end > n:
                    continue

                sub_source = source[start:end]
                sub_target = target[start:end]
                if sub_source not in costs or sub_target not in costs:
                    continue

                dp[end] = min(dp[end], dp[start] + costs[sub_source].get(sub_target, Solution.INFINITY))

        return -1 if dp[n] == Solution.INFINITY else dp[n]
