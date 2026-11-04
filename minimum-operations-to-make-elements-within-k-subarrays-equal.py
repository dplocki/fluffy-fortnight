class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        left, right = SortedList(), SortedList()
        left_sum, right_sum = 0, 0
        ops = [0] * n

        for index, num in enumerate(nums):
            if not left or num <= left[-1]:
                left.add(num)
                left_sum += num
            else:
                right.add(num)
                right_sum += num

            if index >= x:
                num = nums[index - x]
                if num in left:
                    left.remove(num)
                    left_sum -= num
                else:
                    right.remove(num)
                    right_sum -= num

            if len(left) > len(right) + 1:
                num = left.pop()
                right.add(num)
                left_sum -= num
                right_sum += num
            elif len(left) < len(right):
                num = right.pop(0)
                left.add(num)
                left_sum += num
                right_sum -= num

            if index >= x - 1:
                middle = left[-1]
                ops[index] = middle * (len(left) - len(right)) - left_sum + right_sum

        previous = [0] * (n + 1)
        current = [inf] * (n + 1)
        for start in range(1, k + 1):
            for index in range(n + 1):
                current[index] = inf

            for index in range(start * x, n + 1):
                current[index] = min(current[index - 1], previous[index - x] + ops[index - 1])
            previous, current = current, previous

        return previous[n]
