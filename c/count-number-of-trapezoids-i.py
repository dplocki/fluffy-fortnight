class Solution:
    MOD = 10**9 + 7

    def countTrapezoids(self, points: List[List[int]]) -> int:
        lines = defaultdict(int)
        for point in points:
            lines[point[1]] += 1

        pairs_count = [ s * (s - 1) >> 1 for s in lines.values()]
        total_sum = sum(pairs_count)
        sum_of_squares = sum(p * p for p in pairs_count)
        return ((total_sum * total_sum - sum_of_squares) >> 1) % Solution.MOD
