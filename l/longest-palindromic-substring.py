class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = None
        result_size = 0

        for index in range(len(s)):
            tmp, tmp_size  = self.palindrom(s, index, index + 1)
            if tmp_size > result_size:
                result = tmp
                result_size = tmp_size

            tmp, tmp_size = self.palindrom(s, index - 1, index + 1)
            if tmp_size > result_size:
                result = tmp
                result_size = tmp_size

        return result

    def palindrom(self, s: str, left: int, right: int) -> Tuple[str, int]:
        while True:
            if left < 0 or right >= len(s) or s[left] != s[right]:
                return s[left + 1:right], right - left - 1

            left -= 1
            right += 1
