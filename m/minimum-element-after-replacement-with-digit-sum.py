class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(
            sum(self.get_digits(num))
            for num in nums
        )
    
    def get_digits(self, num: int) -> Generator[int, None, None]:
        while num > 0:
            yield num % 10
            num //= 10
