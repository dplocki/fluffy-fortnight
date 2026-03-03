class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def internal(level: int, position: int) -> int:
            if position == 1:
                return 0

            if (position & (position - 1)) == 0:
                return 1

            length = 1 << level
            if (position << 1) < length - 1:
                return internal(level - 1, position)
          
            reversed_position = length - position
            return internal(level - 1, reversed_position) ^ 1

        return str(internal(n, k))
