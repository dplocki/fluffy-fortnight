class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        after = {}

        tmp = nums[-1]
        for index in range(n - 2, -1, -1):
            after[index] = tmp
            if nums[index] < tmp:
                tmp = nums[index]

        result = 0
        tmp = nums[0]
        for index, num in enumerate(nums[1:-1], 1):
            if tmp < num and num < after[index]:
                result += 2
            elif nums[index - 1] < num < nums[index + 1]:
                result += 1

            if num > tmp:
                tmp = num

        return result
