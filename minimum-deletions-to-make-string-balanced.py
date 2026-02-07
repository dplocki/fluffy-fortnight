class Solution:
    def minimumDeletions(self, s: str) -> int:
        result, count = 0, 0
        for letter in s:
            if letter == 'b':
                count += 1
            elif count > 0:
                result += 1
                count -= 1

        return result
