class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.segments = [0] * (self.n << 2)
        self.build(array, 1, 0, self.n - 1)

    def build(self, array: List[int], index: int, left: int, right: int) -> None:
        if left == right:
            self.segments[index] = array[left]
            return

        middle = (left + right) >> 1

        self.build(array, index << 1, left, middle)
        self.build(array, index << 1 | 1, middle + 1, right)

        self.segments[index] = max(self.segments[index << 1], self.segments[index << 1 | 1])

    def query(self, left: int, right: int) -> int:
        if left > right:
            return 0

        def internal(p: int, l: int, r: int) -> int:
            if left <= l and r <= right:
                return self.segments[p]

            middle = (l + r) >> 1
            result = 0

            if left <= middle:
                result = max(result, internal(p << 1, l, middle))

            if right > middle:
                result = max(result, internal(p << 1 | 1, middle + 1, r))

            return result

        return internal(1, 0, self.n - 1)


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        count_ones = s.count("1")

        zero_blocks = []
        block_left = []
        block_right = []

        index = 0
        while index < n:
            start = index

            while index < n and s[index] == s[start]:
                index += 1

            if s[start] == "0":
                zero_blocks.append(index - start)
                block_left.append(start)
                block_right.append(index - 1)

        zero_blocks_lenght = len(zero_blocks)
        if zero_blocks_lenght < 2:
            return [count_ones] * len(queries)

        segment_tree = SegmentTree([l + r for l, r in pairwise(zero_blocks)])
        result = []

        for l, r in queries:
            i = bisect_left(block_right, l)
            j = bisect_right(block_left, r) - 1

            if i > zero_blocks_lenght - 1 or j < 0 or i >= j:
                result.append(count_ones)
                continue

            first_lenght = block_right[i] - max(block_left[i], l) + 1
            last_lenght = min(block_right[j], r) - block_left[j] + 1

            if i + 1 == j:
                result.append(count_ones + first_lenght + last_lenght)
                continue

            value1 = first_lenght + zero_blocks[i + 1]
            value2 = zero_blocks[j - 1] + last_lenght
            value3 = segment_tree.query(i + 1, j - 2)

            result.append(count_ones + max(value1, value2, value3))

        return result
