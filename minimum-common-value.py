class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        iter1 = iter(nums1)
        iter2 = iter(nums2)
        
        num1 = next(iter1, -1)
        num2 = next(iter2, -1)

        while num1 != num2:
            if num1 < num2:
                num1 = next(iter1, -1)

            if num2 < num1:
                num2 = next(iter2, -1)

        return num1
