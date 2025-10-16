class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        cache = {}
        for index in range(n - 1, -1, -1):
            cache[index] = energy[index] + cache.get(index + k, 0)
        
        return max(cache.values())
