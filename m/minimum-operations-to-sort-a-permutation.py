class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        start = nums.index(0)

        is_ascending = True
        is_desceding = True

        for index in range(1, n):
            value = nums[(start + index) % n]

            if value != index:
                is_ascending = False

            if value != n - index:
                is_desceding = False

            if not is_ascending and not is_desceding:
                return -1

        if is_ascending:
            return min(start, n - start + 2)

        return min(n - start, start + 2)
