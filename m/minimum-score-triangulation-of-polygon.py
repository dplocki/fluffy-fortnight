class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @cache
        def internal(left_index: int, right_index: int) -> int:
            if left_index + 1 == right_index:
                return 0

            return min(
                internal(left_index, split_index) \
                 + internal(split_index, right_index) \
                 + values[left_index] * values[split_index] * values[right_index]
                for split_index in range(left_index + 1, right_index)
            )
        
        return internal(0, len(values) - 1)
