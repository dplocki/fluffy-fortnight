class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda a: (Solution.count_set_bits(a), a))
        
    def count_set_bits(n: int) -> int:
        count = 0
        while (n):
            count += n & 1
            n >>= 1

        return count
