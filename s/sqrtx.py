class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x

        while low < high:
            mid = (low + high + 1) >> 1

            if x // mid >= mid:
                low = mid
            else:
                high = mid - 1
        
        return low
