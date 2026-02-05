class Solution:
   def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n, total = len(nums), nums[0]
        window, subarrays_costs = SortedList(nums[1:dist+2]), SortedList()

        def balance(total: int) -> int:
            while len(subarrays_costs) < k - 1 and window:
                val = window.pop(0)
                subarrays_costs.add(val)
                total += val

            while len(subarrays_costs) > k - 1:
                val = subarrays_costs.pop(-1)
                window.add(val)
                total -= val

            return total

        total = balance(total)
        result = total

        for i in range(dist+2, n):
            left = nums[i - dist - 1]

            if left in subarrays_costs:
                subarrays_costs.remove(left)
                total -= left

            if left in window:
                window.remove(left)

            right = nums[i]
            if not subarrays_costs or right < subarrays_costs[-1]:
                subarrays_costs.add(right)
                total += right
            else:
                window.add(right)

            total = balance(total)
            result = min(result, total)

        return result
