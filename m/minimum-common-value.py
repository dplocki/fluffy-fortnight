class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        iter1 = iter(nums1)
        iter2 = iter(nums2)
        
        num1 = next(iter1, None)
        num2 = next(iter2, None)

        while num1 != None and num2 != None:
            if num1 == num2:
                return num1

            if num1 < num2:
                num1 = next(iter1, None)
            elif num1 > num2:
                num2 = next(iter2, None)

        return -1
