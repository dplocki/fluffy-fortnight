class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix_sum, prev = [0], 0
        for value in stoneValue:
            prefix_sum.append(prev + value)
            prev = prefix_sum[-1]

        @cache
        def internal(left: int, right: int) -> int:
            if left >= right:
                return 0

            result = 0
            for split in range(left + 1, right + 1):
                left_row = prefix_sum[split] - prefix_sum[left]
                right_row = prefix_sum[right + 1] - prefix_sum[split]
                
                if left_row > right_row:
                    result = max(result, right_row + internal(split, right))
                elif left_row < right_row:
                    result = max(result, left_row + internal(left, split - 1))
                else:
                    result = max(result, left_row + max(internal(left, split - 1), internal(split, right)))

            return result

        return internal(0, len(stoneValue) - 1)
