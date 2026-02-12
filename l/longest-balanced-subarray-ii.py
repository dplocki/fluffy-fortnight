class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.size = 4 * n
        self.sum = [0] * self.size
        self.min = [0] * self.size
        self.max = [0] * self.size

    def _pull(self, node: int):
        left, right = node * 2, node * 2 + 1

        self.sum[node] = self.sum[left] + self.sum[right]
        self.min[node] = min(self.min[left], self.sum[left] + self.min[right])
        self.max[node] = max(self.max[left], self.sum[left] + self.max[right])

    def update(self, idx: int, val: int):
        node, left, right = 1, 0, self.n - 1
        path = []

        while left != right:
            path.append(node)
            m = (left + right) >> 1
            if idx <= m:
                node = node * 2
                right = m
            else:
                node = node * 2 + 1
                left = m + 1

        self.sum[node] = val
        self.min[node] = val
        self.max[node] = val

        while path:
            self._pull(path.pop())

    def find_rightmost_prefix(self, target: int = 0) -> int:
        node, left, right, sum_before = 1, 0, self.n - 1, 0

        def _exist(node: int, sum_before: int):
            return self.min[node] <= target - sum_before <= self.max[node]

        if not _exist(node, sum_before):
            return -1

        while left != right:
            m = (left + right) >> 1
            lchild, rchild = node * 2, node * 2 + 1

            sum_before_right = self.sum[lchild] + sum_before
            if _exist(rchild, sum_before_right):
                node = rchild
                left = m + 1
                sum_before = sum_before_right
            else:
                node = lchild
                right = m

        return left


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        stree = SegmentTree(n)
        first = dict()

        result = 0
        for left in reversed(range(n)):
            num = nums[left]
    
            if num in first:
                stree.update(first[num], 0)

            first[num] = left
            stree.update(left, 1 if num % 2 == 0 else -1)

            right = stree.find_rightmost_prefix(target=0)
            if right >= left:
                result = max(result, right - left + 1)

        return result
