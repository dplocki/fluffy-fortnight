class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = defaultdict(list) 
        dp[0].append([])

        for candidate in candidates:
            for index in range(candidate, target + 1):
                for option in dp[index - candidate]:
                    dp[index].append(option + [candidate])

        return dp[target]
