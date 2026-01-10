class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        the_smallest = abs(matrix[0][0])
        sum_of_all, negatives = 0, 0
        is_zero_present = False

        for row in matrix:
            for cell in row:
                if cell == 0:
                    is_zero_present = True

                if cell < 0:
                    negatives += 1
                    cell *= -1

                sum_of_all += cell
                the_smallest = min(the_smallest, cell)

        if is_zero_present or negatives % 2 == 0:
            return sum_of_all

        return sum_of_all - (the_smallest << 1)
