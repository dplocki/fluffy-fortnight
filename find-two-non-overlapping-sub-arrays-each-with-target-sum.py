class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        left, right = 0, 0
        window_len, window_sum = 1, arr[0]
        suffix = [inf] * n
        result = inf

        while True:
            if window_sum == target:
                if right - window_len >= 0:
                    result = min(result, window_len + suffix[right - window_len])

                suffix[right] = min(window_len, suffix[right])

            if window_sum < target:
                right += 1
                if right == n:
                    break

                suffix[right] = suffix[right - 1]
                window_sum += arr[right]
                window_len += 1

            elif window_sum >= target:
                window_sum -= arr[left]
                window_len -= 1
                left += 1

                if left == n:
                    break

        return -1 if result == inf else result
