class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        dp, n = {}, 0

        for index, num in enumerate(nums):
            if num not in dp:
                dp[num] = []
            
            dp[num].append(index)
            n += 1
        
        def internal(query: int):
            for num in dp.get(nums[query], []):
                if num == query:
                    continue 
                
                d = abs(num - query)
                yield d
                yield n - d
        
        return list(
            min(internal(query), default=-1)
            for query in queries
        )
