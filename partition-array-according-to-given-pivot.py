class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return list(chain(
            (num for num in nums if num < pivot),
            (num for num in nums if num == pivot),
            (num for num in nums if num > pivot)
        ))
