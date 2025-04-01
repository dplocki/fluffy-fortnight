class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums_count = len(nums)
        result = set()

        for index1 in range(0, nums_count - 3):
            target1 = target - nums[index1]
            for index2 in range(index1 + 1, nums_count - 2):
                target2 = target1 - nums[index2]
                for index3 in range(index2 + 1, nums_count - 1):
                    target3 = target2 - nums[index3]
                    for index4 in range(index3 + 1, nums_count):
                        target4 = target3 - nums[index4]
                        if target4 == 0:
                            result.add(tuple(sorted((nums[index1], nums[index2], nums[index3], nums[index4]))))

        return list(result)

