class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_nums = [n % 2 == 0 for n in nums]
        all_odd = 1 if not even_nums[0] else 0
        all_even = 1 if even_nums[0] else 0
        all_swap = current_swap = 0
        last_swap_group_end = None

        for a, b in zip(even_nums, even_nums[1:]):
            if a and b:
                all_even += 1
                all_swap += current_swap
                current_swap = 0
            elif not a and not b:
                all_odd += 1
                all_swap += current_swap
                current_swap = 0
            elif a or b:
                if b:
                    all_even += 1
                else:
                    all_odd += 1

                if current_swap == 0 and last_swap_group_end == a:
                    current_swap -= 1

                current_swap += 1 if current_swap > 0 else 2
                last_swap_group_end = b

        all_swap += current_swap

        return max(all_odd, all_even, all_swap)
