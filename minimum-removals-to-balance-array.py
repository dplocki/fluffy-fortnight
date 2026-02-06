class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        to_checked = [(0, 0, n)]
        heapify([])

        while to_checked:
            cost, left, right = heappop(to_checked)
            if nums[left] * k >= nums[right - 1] or left + 1 >= right:
                return cost

            cost += 1
            heappush(to_checked, (cost, left + 1, right))
            heappush(to_checked, (cost, left, right - 1))
