MOD = (10 ** 9) + 7


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        count = 0

        for start_index in range(n):
            current_sum = 0

            for end_index in range(start_index, n):
                current_sum += arr[end_index] & 1

                if current_sum & 1 != 0:
                    count += 1

        return int(count % MOD)
