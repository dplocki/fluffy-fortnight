class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        next_zero_index = [n] * (n + 1)

        for index in range(n - 1, -1, -1):
            next_zero_index[index] = index if s[index] == '0' else next_zero_index[index + 1]

        result = 0
        for start in range(n):
            zeros_count = 1 if s[start] == '0' else 0
            chunk_end = start

            while chunk_end < n and zeros_count * zeros_count <= n:
                ones_count = (next_zero_index[chunk_end + 1] - start) - zeros_count
                if ones_count >= zeros_count * zeros_count:
                    result += min(next_zero_index[chunk_end + 1] - chunk_end, ones_count - zeros_count * zeros_count + 1)

                chunk_end = next_zero_index[chunk_end + 1]
                zeros_count += 1

        return result
