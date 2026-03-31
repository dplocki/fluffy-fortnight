class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        result = ['a'] * (n + m - 1)
        letters = {}

        for start, value in enumerate(str1):
            if value == 'F':
                continue

            for i, letter in enumerate(str2, start):
                if letters.get(i, False) and result[i] != letter:
                    return ''

                result[i] = letter
                letters[i] = True

        for start, value in enumerate(str1):
            if value == 'T':
                continue

            if any(result[i] != letter for i, letter in enumerate(str2, start)):
                continue

            for i in range(start + m - 1, start - 1, -1):
                if letters.get(i, False):
                    continue

                result[i] = 'b'
                break
            else:
                return ''

        return ''.join(result)
