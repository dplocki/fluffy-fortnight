class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        result, n1, n2 = 0, len(nums1), len(nums2)
        for i in range(min(n1, n2)):
            for j in range(i, n2):
                if nums1[i] <= nums2[j]:
                    result = max(result, j - i)
        
        return result
