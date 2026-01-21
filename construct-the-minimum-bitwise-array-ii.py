class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        return list(map(self.find_a, nums))

    def find_a(self, num: int) -> int:
        if num == 2:
            return -1

        for bit_position in range(1, 32):
            if ((num >> bit_position) & 1) == 0:
                answer = num ^ (1 << (bit_position - 1))
                return answer

        return -1
