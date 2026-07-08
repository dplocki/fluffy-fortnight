MOD = 10**9 + 7

max_s_lenght = 10 ** 5 + 1
pow10 = [1] * max_s_lenght
for i in range(1, max_s_lenght):
    pow10[i] = pow10[i - 1] * 10 % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        length_prefix_table = [0] * (n + 1)
        sum_prefix_table = [0] * (n + 1)
        substring_prefix_table = [0] * (n + 1)

        for index, character in enumerate(s):
            digit = int(character)

            length_prefix_table[index + 1] = length_prefix_table[index] + (1 if digit > 0 else 0)
            sum_prefix_table[index + 1] = sum_prefix_table[index] + digit
            substring_prefix_table[index + 1] = (substring_prefix_table[index] * 10 + digit) % MOD if digit > 0 else substring_prefix_table[index]

        return list(
            (sum_prefix_table[end + 1] - sum_prefix_table[start]) *
            (
                substring_prefix_table[end + 1] - 
                substring_prefix_table[start] * pow10[length_prefix_table[end + 1] - length_prefix_table[start]]
            ) % MOD
            for start, end in queries)
