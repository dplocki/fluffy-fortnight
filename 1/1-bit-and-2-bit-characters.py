class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        single_bit = False
        index = 0
        while index < n:
            if bits[index] == 0:
                index += 1
                single_bit = True
                continue

            index += 2
            single_bit = False

        return single_bit
