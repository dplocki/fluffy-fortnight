class Solution:
    def processStr(self, s: str, k: int) -> str:
        string_size = 0
        for operation in s:
            if operation == '*':
                if string_size == 0:
                    continue

                string_size -= 1
            elif operation == '#':
                string_size *= 2
            elif operation == '%':
                pass
            else:
                string_size += 1

        if k >= string_size:
            return '.'

        for operation in reversed(s):
            if operation == '%':
                k = string_size - k - 1
            elif operation == '*':
                string_size += 1
            elif operation == '#':
                if k + 1 > (string_size + 1) // 2:
                    k -= string_size // 2

                string_size = (string_size + 1) // 2
            else:
                if k + 1 == string_size:
                    return operation

                string_size -= 1

        return '.'
