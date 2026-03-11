class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        zeros_from_right, n = [], len(grid)

        for row in grid:
            zero_from_right = 0
            for cell in reversed(row):
                if cell == 0:
                    zero_from_right += 1
                else:
                    break

            zeros_from_right.append(zero_from_right)

        result = 0
        for new_place in range(n):
            current_place = None
            for test_row in range(new_place, n):
                if zeros_from_right[test_row] < n - new_place - 1:
                    continue
                
                current_place = test_row
                break

            if current_place == None:
                return -1

            result += current_place - new_place
            while current_place > new_place:
                zeros_from_right[current_place -1], zeros_from_right[current_place] = zeros_from_right[current_place], zeros_from_right[current_place - 1]
                current_place -= 1

        return result
