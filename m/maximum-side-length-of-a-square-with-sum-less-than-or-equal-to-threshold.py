class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        table_sum = {}

        for ir, row in enumerate(mat):
            for ic, value in enumerate(row):
                table_sum[ir, ic] = value + table_sum.get((ir - 1, ic), 0) + table_sum.get((ir, ic - 1), 0) - table_sum.get((ir - 1, ic - 1), 0)

        def there_is_square(size: int) -> bool:
            return any(
                (table_sum[ir + size - 1, ic + size - 1]
                - table_sum.get((ir - 1, ic + size - 1), 0)
                - table_sum.get((ir + size - 1, ic - 1), 0)
                + table_sum.get((ir - 1, ic - 1), 0)) <= threshold
                for ir in range(m - size + 1)
                for ic in range(n - size + 1))

        left, right = 0, min(m, n)
        while left < right:
            midle = (left + right + 1) >> 1
            if there_is_square(midle):
                left = midle
            else:
                right = midle - 1

        return left
