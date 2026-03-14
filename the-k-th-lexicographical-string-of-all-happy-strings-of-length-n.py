class Solution:
    LETTERS = { 'a': 'bc', 'b': 'ac', 'c': 'ab' }

    def getHappyString(self, n: int, k: int) -> str:
        block_size = 2 ** (n - 1)
        k -= 1
        if k >= 3 * block_size:
            return ''

        result = ['abc'[k // block_size]]
        k %= block_size

        for _ in range(n - 1):
            block_size >>= 1
            result.append(Solution.LETTERS[result[-1]][k // block_size])
            k %= block_size

        return ''.join(result)
