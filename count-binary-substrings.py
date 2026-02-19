class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return sum(
            min(a, b)
            for a, b in pairwise(self.split_into_groups(s)))

    def split_into_groups(self, s):
        bits = iter(s)
        prev = next(bits)
        group = 1

        for bit in bits:
            if prev != bit:
                yield group
                prev = bit
                group = 1
            else:
                group += 1

        yield group
