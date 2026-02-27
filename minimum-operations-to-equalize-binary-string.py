class Solution:
    def minOperations(self, s: str, k: int) -> int:
        visited = set()
        to_check = [(0, s.count('1'), s.count('0'))]

        while to_check:
            steps, ones, zeros = heappop(to_check)
            if (zeros, ones) in visited:
                continue

            visited.add((zeros, ones))
            if zeros == 0:
                return steps

            steps += 1
            for d_zeros in range(min(zeros, k) + 1):
                d_ones = k - d_zeros
                if d_ones > ones:
                    continue

                new_zeros = zeros - d_zeros + d_ones
                new_ones = ones - d_ones + d_zeros
                if (new_zeros >= 0 and new_ones >= 0) and (new_zeros, new_ones) not in visited:
                    heappush(to_check, (steps, new_ones, new_zeros))

        return -1
