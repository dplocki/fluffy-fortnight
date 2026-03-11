class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int(f'{n:b}'.replace('0', 'a').replace('1', '0').replace('a', '1'), 2)
