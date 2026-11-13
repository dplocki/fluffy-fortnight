class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        reversed_nums = nums[::-1]
        stack = deque()
        maxium_sum, elements = 0, 0
        left = 0

        for right, num in enumerate(reversed_nums):
            count = 1
            while stack and stack[-1][0] <= num:
                v, c = stack.pop()
                maxium_sum -= v * c
                count += c

            stack.append([num, count])
            maxium_sum += num * count
            elements += num

            while maxium_sum - elements > k:
                maxium_sum -= stack[0][0]
                stack[0][1] -= 1
                if stack[0][1] == 0:
                    stack.popleft()

                elements -= reversed_nums[left]
                left += 1

            result += right - left + 1

        return result
