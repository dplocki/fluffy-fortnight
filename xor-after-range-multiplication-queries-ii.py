class Solution:
    MOD = 10**9 + 7

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        limit = math.isqrt(n)
        smaller_k = defaultdict(list)

        for l, r, k, v in queries: 
            if k >= limit:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % Solution.MOD
            else:
                smaller_k[k].append((l, r, v))

        for k, query_list in smaller_k.items():
            diff = [1] * n
            
            for l, r, v in query_list:
                diff[l] = (diff[l] * v) % Solution.MOD
                
                steps = (r - l) // k
                nxt = l + (steps + 1) * k
                if nxt < n:
                    diff[nxt] = (diff[nxt] * pow(v, -1, Solution.MOD)) % Solution.MOD
                    
            for i in range(n):
                if i >= k:
                    diff[i] = (diff[i] * diff[i - k]) % Solution.MOD

                nums[i] = (nums[i] * diff[i]) % Solution.MOD

        return reduce(operator.xor, nums)
