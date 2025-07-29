class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        result = 0
        tmp_result = 0

        while numbers:
            tmp = min(numbers)
            numbers.remove(tmp)
            tmp_result = 1

            while tmp + 1 in numbers:
                numbers.remove(tmp + 1)
                tmp_result += 1
                tmp += 1

            result = max(result, tmp_result)

        return result
