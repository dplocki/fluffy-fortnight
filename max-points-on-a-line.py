class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        def get_indentication(ax: int, ay: int, bx: int, by: int) -> float:
            dx, dy = bx - ax, by - ay

            if dx == 0:
                return inf, ax, 0

            g = gcd(abs(dx), abs(dy))
            dx, dy = dx // g, dy // g
            if dx < 0:
                dx, dy = -dx, -dy

            b_num = ay * dx - dy * ax
            return dy, dx, b_num

        counter = Counter()

        if len(points) < 2:
            return 1

        for ((ax, ay), (bx, by)) in combinations(points, 2):
            counter[get_indentication(ax, ay, bx, by)] += 1

        pairs = counter.most_common()[0][1]
        return (1 + isqrt(1 + 8 * pairs)) // 2
