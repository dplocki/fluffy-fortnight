class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return list(chain.from_iterable(map(int, str(num)) for num in nums))
