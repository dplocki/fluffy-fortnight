class Solution:
    def minFlips(self, s: str) -> int:
        result, n = 10**6, len(s)

        for m in range(n - 1):
            zero_start_odd = 0
            for index in range(n):
                diggit = s[(index + m) % n]
                if index % 2 == 0:
                    if diggit != '1':
                        zero_start_odd += 1
                else:
                    if diggit == '1':
                        zero_start_odd += 1
            
            result = min(result, zero_start_odd, n - zero_start_odd)

        return result
