class Solution:
    def check(self, nums: List[int]) -> bool:
        breaks = 1

        for a, b in chain(pairwise(nums), ((nums[-1], nums[0]),)):
            if a > b:
                if breaks == 0:
                    return False
                breaks -= 1

        return True    
