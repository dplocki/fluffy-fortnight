class QueryTree:
    def __init__(self, nums: List[int], n: int):
        self.n = n
        self.nodes = [(0, 0)] * (n * 4)

        self.build(nums, 1, 0, n - 1)

    def build(self, nums: List[int], node_index: int, left: int, right: int):
        if left == right:
            self.nodes[node_index] = (nums[left], nums[left])
            return

        middle = left + ((right - left) >> 1)

        self.build(nums, node_index << 1, left, middle)
        self.build(nums, (node_index << 1) + 1, middle + 1, right)
        self.nodes[node_index] = (
            max(self.nodes[node_index << 1][0], self.nodes[(node_index << 1) + 1][0]),
            min(self.nodes[node_index << 1][1], self.nodes[(node_index << 1) + 1][1])
        )

    def internal_query(self, node_index: int, min_left: int, max_right: int, left: int, right: int) -> Tuple[int, int]:
        if left > max_right or right < min_left:
            return (-inf, inf)
        
        if left <= min_left and right >= max_right:
            return self.nodes[node_index]

        middle = min_left + ((max_right - min_left) >> 1)
        left_max, left_min = self.internal_query(node_index << 1, min_left, middle, left, right)
        right_max, right_min = self.internal_query((node_index << 1) + 1, middle + 1, max_right, left, right)

        return max(left_max, right_max), min(left_min, right_min)

    def query(self, left: int, right: int) -> int:
        node_max, node_min = self.internal_query(1, 0, self.n - 1, left, right)
        return node_max - node_min


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        query_tree = QueryTree(nums, n)
        result = 0
        start = (0, n - 1)
        seen = {start}
        possibilities = []
        heappush(possibilities, (-query_tree.query(*start), *start))

        for _ in range(k):
            value, left, right = heappop(possibilities)
            result -= value

            for new_range in [(left + 1, right), (left, right - 1)]:
                l, r = new_range
                if l <= r and new_range not in seen:
                    heappush(possibilities, (-query_tree.query(l, r), l, r))
                    seen.add(new_range)

        return result
