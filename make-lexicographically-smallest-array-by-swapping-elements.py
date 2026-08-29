class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n, sorted_nums = len(nums), sorted(nums)

        current_group = 0
        nums_groups = { sorted_nums[0]: current_group }
        groups = { 0: deque([sorted_nums[0]]) }

        for i in range(1, n):
            if sorted_nums[i] - sorted_nums[i - 1] > limit:
                current_group += 1
                groups[current_group] = deque()

            nums_groups[sorted_nums[i]] = current_group
            groups[current_group].append(sorted_nums[i])

        return [
            groups[nums_groups[nums[i]]].popleft()
            for i in range(n)
        ]
