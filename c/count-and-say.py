class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(1, n):
            result = ''.join(
                f'{count}{digit}'
                for digit, count in self.split_into_tokens(result))

        return result

    def split_into_tokens(self, n: str):
        prev = n[0]
        group_size = 0

        for digit in n:
            if digit == prev:
                group_size += 1
            else:
                yield prev, group_size
                group_size = 1

            prev = digit

        yield prev, group_size
