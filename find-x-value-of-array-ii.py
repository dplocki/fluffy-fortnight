class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        n = len(nums)
        size = 2 << n.bit_length()
        self.tree = [[0] * (k + 1) for _ in range(size)]
        self.build(nums, 1, 0, n - 1)

    def build_leaf(self, o: int, value: int) -> None:
        info = [0] * (self.k + 1)
        r = value % self.k
        info[r] = 1
        info[self.k] = r
        self.tree[o] = info

    def merge_pre(self, left: List[int], right: List[int]) -> List[int]:
        result = [0] * (self.k + 1)

        mul_L = left[self.k]
        mul_R = right[self.k]

        result[self.k] = (mul_L * mul_R) % self.k

        for x in range(self.k):
            result[x] = left[x]

        for x in range(self.k):
            result[(mul_L * x) % self.k] += right[x]

        return result

    def maintain(self, o: int) -> None:
        self.tree[o] = self.merge_pre(
            self.tree[o * 2],
            self.tree[o * 2 + 1],
        )

    def build(self, nums: List[int], o: int, l: int, r: int) -> None:
        if l == r:
            self.build_leaf(o, nums[l])
            return

        o2 = o << 1
        m = (l + r) // 2
        self.build(nums, o2, l, m)
        self.build(nums, o2 + 1, m + 1, r)
        self.maintain(o)

    def update(self, o: int, l: int, r: int, index: int, value: int) -> None:
        if l == r:
            self.build_leaf(o, value)
            return

        m = (l + r) // 2
        if index <= m:
            self.update(o * 2, l, m, index, value)
        else:
            self.update(o * 2 + 1, m + 1, r, index, value)

        self.maintain(o)

    def query(self, o: int, l: int, r: int, L: int, R: int) -> List[int]:
        if L <= l and r <= R:
            return self.tree[o]

        o2 = o << 1
        m = (l + r) // 2
        if R <= m:
            return self.query(o2, l, m, L, R)
        if L > m:
            return self.query(o2 + 1, m + 1, r, L, R)

        left = self.query(o2, l, m, L, R)
        right = self.query(o2 + 1, m + 1, r, L, R)
        return self.merge_pre(left, right)


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        segment = SegmentTree(nums, k)

        result = []
        for index, value, start, x in queries:
            segment.update(1, 0, n - 1, index, value)
            query_result = segment.query(1, 0, n - 1, start, n - 1)
            result.append(query_result[x])

        return result
