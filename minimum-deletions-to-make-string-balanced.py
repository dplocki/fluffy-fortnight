class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_before = []

        n = 0
        count = 0
        for letter in s:
            if letter == 'b':
                count += 1

            b_before.append(count)
            n += 1
       
        result = n
        count = 0
        for index in range(n - 1, -1, -1):
            if s[index] == 'a':
                count += 1

            result = min(result, b_before[index] + count - 1)

        return result
