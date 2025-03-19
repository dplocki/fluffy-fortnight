class Solution:
    def median(self, array):
        array_size = len(array)
        index = array_size // 2

        if array_size % 2 == 0:
            return (array[index] + array[index + 1]) / 2
        
        return array[index]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))
