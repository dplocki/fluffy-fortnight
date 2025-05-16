class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = defaultdict(set) 
        dp[0].add(tuple())

        for index in range(target + 1):
            for candidate in candidates:
                dp[index].update(
                    tuple(sorted(option + (candidate, )))
                    for option in dp[index - candidate]
                )

        return [list(i) for i in dp[target]]
