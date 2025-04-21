class Solution:
    def jump(self, nums: List[int]) -> int:
        last_index = len(nums) - 1
        possibilites = deque([(0, 0)])

        while possibilites:
            current_index, current_jumps_count = possibilites.popleft()
            if current_index == last_index:
                return current_jumps_count

            next_jump_count = current_jumps_count + 1
            for delta in range(1, nums[current_index] + 1):
                possibilites.append((current_index + delta, next_jump_count))
