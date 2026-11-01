def sort_key(n: int) -> int:
    return (sum(map(int, str(n))), n)


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        target_positions = {
            num: index
            for index, num in enumerate(sorted(nums, key=sort_key))
        }

        result = len(nums)
        visited = set()

        for num in nums:
            if num in visited:
                continue
            
            result -= 1
            current = num

            while current not in visited:
                visited.add(current)
                current = nums[target_positions[current]]

        return result
