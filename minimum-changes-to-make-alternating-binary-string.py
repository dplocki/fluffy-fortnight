class Solution:
    def minOperations(self, s: str) -> int:
        zero_start_odd, zero_start_even = 0, 0

        for index, diggit in enumerate(s):
            if index % 2 == 0:
                if diggit == '1':
                    zero_start_even += 1
                else:
                    zero_start_odd += 1
            else:
                if diggit == '1':
                    zero_start_odd += 1
                else:
                    zero_start_even += 1
        
        return min(zero_start_odd, zero_start_even)
