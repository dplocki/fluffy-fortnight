class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(1, n):
            result = ''.join(
                f'{len(token)}{token[0]}'
                for token in self.split_into_tokens(result))

        return result

    def split_into_tokens(self, n: str):
        prev = n[0]
        group = ''

        for digit in n:
            if digit == prev:
                group += digit
            else:
                yield group
                group = digit

            prev = digit

        yield group
