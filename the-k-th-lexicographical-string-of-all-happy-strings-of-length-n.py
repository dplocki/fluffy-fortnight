class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings_count = 2 ** (n - 1)
        if k > 3 * happy_strings_count:
            return ''

        k -= 1
        result = prev_letter = 'abc'[k // happy_strings_count]
        k %= happy_strings_count

        for _ in range(n - 1):
            happy_strings_count >>= 1
            match [prev_letter, k // happy_strings_count]:
                case ['a', 0]: prev_letter = 'b'
                case ['a', 1]: prev_letter = 'c'
                case ['b', 0]: prev_letter = 'a'
                case ['b', 1]: prev_letter = 'c'
                case ['c', 0]: prev_letter = 'a'
                case ['c', 1]: prev_letter = 'b'

            k %= happy_strings_count
            result += prev_letter

        return result
