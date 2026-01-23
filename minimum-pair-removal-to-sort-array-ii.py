class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        next_node_map = {i:(i + 1) for i in range(n)}

        while True:
            if n == 1:
                return result

            is_non_decreasing = True
            minimal_pair_sum = float('inf')
            minimal_pair_sum_index = -1

            current_index = 0
            current_node_value = nums[current_index]

            for _ in range(n - 1):
                next_index = next_node_map[current_index]
                next_node_value = nums[next_index]

                if current_node_value > next_node_value:
                    is_non_decreasing = False

                pair_sum = current_node_value + next_node_value
                if pair_sum < minimal_pair_sum:
                    minimal_pair_sum = pair_sum
                    minimal_pair_sum_index = current_index

                current_index = next_index
                current_node_value = next_node_value

            if is_non_decreasing:
                return result

            result += 1
            nums[minimal_pair_sum_index] = minimal_pair_sum
            next_node_map[minimal_pair_sum_index] = next_node_map[next_node_map[minimal_pair_sum_index]]
            n -= 1
