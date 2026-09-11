class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set(
            map(lambda p: int(''.join(p)), permutations(map(str, digits), 3))
        )

        return sum(1 for n in numbers if n & 1 == 0 and n > 99)
