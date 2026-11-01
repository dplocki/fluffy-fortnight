MOD = 10 ** 9 + 7


class SegmentTreeNode:
    def __init__(self, low: int, high: int) -> None:
        self.low = low
        self.high = high
        self.value = 0
        self.lazy = 0

        if low + 1 < high:
            middle = (low + high) >> 1
            self.left = SegmentTreeNode(low, middle)
            self.right = SegmentTreeNode(middle, high)

    def update(self, value: int) -> int:
        self.lazy += value
        self.value += value * (self.high - self.low)

    def query(self, low: int, high: int) -> int:
        if self.low >= low and self.high <= high:
            result = self.value
            self.update(1)
            return result

        middle = (self.low + self.high) >> 1
        result = 0
        self.left.update(self.lazy)
        self.right.update(self.lazy)
        self.lazy = 0

        if low < middle:
            result += self.left.query(low, high)

        if high > middle:
            result += self.right.query(low, high)

        self.value = self.left.value + self.right.value
        return result


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        last_index_dict = {}
        segment_tree = SegmentTreeNode(0, len(nums))
        result = 0
        current_result = 0

        for index, num in enumerate(nums):
            last_index = last_index_dict.get(num, -1) + 1
            current_result = (
                current_result + index - last_index + 1 + (segment_tree.query(last_index, index + 1) << 1)
            ) % MOD
            result += current_result
            last_index_dict[num] = index

        return result % MOD
