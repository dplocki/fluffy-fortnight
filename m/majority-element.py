class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        counter = 0

        for num in nums:
            if counter == 0:
                candidate = num
                counter = 1
            elif num == candidate:
                counter += 1
            else:
                counter -= 1

        return candidate
