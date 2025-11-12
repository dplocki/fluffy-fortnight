class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        previous = set()
        result = []

        for num in nums:
            if num in previous:
                result.append(num)
                if len(result) == 2:
                    return result
            else:
                previous.add(num)

        return result
