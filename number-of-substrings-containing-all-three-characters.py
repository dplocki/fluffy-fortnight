class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        close_a = [None] * n
        close_b = [None] * n
        close_c = [None] * n

        last_a = last_b = last_c = None

        for index, c in enumerate(s):
            if c == 'a':
                last_a = index
            elif c == 'b':
                last_b = index
            elif c == 'c':
                last_c = index

            close_a[index] = last_a
            close_b[index] = last_b
            close_c[index] = last_c

        result = 0
        for index in range(n - 1, -1, -1):
            if close_a[index] == None or close_b[index] == None or close_c[index] == None:
                continue

            substring_start = min(close_a[index], close_b[index], close_c[index])
            result += substring_start + 1

        return result
