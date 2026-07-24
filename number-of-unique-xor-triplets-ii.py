class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        maximum = max(nums)
        maximum_bits = 1
        while maximum_bits <= maximum:
            maximum_bits <<= 1

        pairs = set()
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                pairs.add(nums[i] ^ nums[j])

        triples = set()
        for x in range(maximum_bits):
            if x not in pairs:
                continue
            
            for v in nums:
                triples.add(x ^ v)

        return len(triples)
