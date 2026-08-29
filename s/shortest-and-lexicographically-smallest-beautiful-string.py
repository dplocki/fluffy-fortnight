class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ''

        result = s
        left, ones = 0, 0

        for right, digit in enumerate(s):
            if digit == '1':
                ones += 1

            while ones > k or s[left] == '0':
                if s[left] == '1':
                    ones -= 1

                left += 1

            if ones == k:
                temp = s[left:right + 1]
                temp_size = right - left + 1

                if temp_size < len(result) or temp_size == len(result) and temp < result:
                    result = temp

        return result
