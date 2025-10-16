class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainders = Counter(num % value for num in nums)
        
        for i in count(0):
            remainder = i % value
            if remainders[remainder] == 0:
                return i

            remainders[remainder] -= 1
