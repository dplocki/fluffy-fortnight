class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        def internal(result: str, num: int, sum: int):
            if sum < 0:
                return None

            if num == 0:
                return result if sum == 0 else None

            for d in range(9, -1, -1):
                local_result = internal(result, num - 1, sum - d)
                if local_result is not None:
                    return str(d) + local_result

            return None


        return internal('', num, sum) or ''
