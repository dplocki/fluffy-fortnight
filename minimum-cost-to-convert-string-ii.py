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

        for a, b, c in zip(original, changed, cost):
            costs[a][b] = min(c, costs[a].get(b, Solution.INFINITY))

        for b in nodes:
            for a in nodes:
                for c in nodes:
                    costs[a][c] = min(costs[a].get(b, Solution.INFINITY) + costs[b].get(c, Solution.INFINITY), costs[a].get(c, Solution.INFINITY))

        lengths = sorted(set(map(len, original)))
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
                    break
                
                substring = source[start:end]
                if substring not in costs:
                    continue

                dp[end] = min(dp[end], dp[start] + costs[substring].get(target[start:end], Solution.INFINITY))

        return  -1 if dp[n] == Solution.INFINITY else dp[n]
