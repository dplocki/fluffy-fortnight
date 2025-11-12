class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones_counter = nums.count(1)

        if ones_counter > 0:
            return n - ones_counter

        minimum = n << 1
        for index_start in range(n):
            current_gcd = 0

            for index_end in range(index_start, n):
                current_gcd = math.gcd(current_gcd, nums[index_end])

                if current_gcd == 1:
                    minimum = min(minimum, index_end - index_start + 1)

        if minimum > n:
            return -1

        return n - 1 + minimum - 1
