class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        state = 0
        for a, b in pairwise(nums):
            if a == b:
                return False
          
            match state:
                case 0:
                    if a > b:
                        return False
                    
                    state = 1
                case 1:
                    if a > b:
                        state = 2

                case 2:
                    if a < b:
                        state = 3

                case 3:
                    if a > b:
                        return False

        return state == 3
