class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        tree = [[] for _ in range(n)]

        for u, v in hierarchy:
            tree[u - 1].append(v - 1)


        def merge(list_a: list[int], list_b: list[int]) -> list[int]:
            merged = [-math.inf] * len(list_a)
            for i, a in enumerate(list_a):
                for j in range(len(list_a) - i):
                    merged[i + j] = max(merged[i + j], a + list_b[j])

            return merged


        @cache
        def dp(u: int, parent: int) -> tuple[list[int], list[int]]:
            no_discount = [0] * (budget + 1)
            with_discount = [0] * (budget + 1)

            for v in tree[u]:
                if v == parent:
                    continue

                employee_no_discount, employee_with_discount = dp(v, u)
                no_discount = merge(no_discount, employee_no_discount)
                with_discount = merge(with_discount, employee_with_discount)

            result_without_discount = no_discount[:]
            result_with_discount = no_discount[:]

            full_cost = present[u]
            for b in range(full_cost, budget + 1):
                profit = future[u] - full_cost
                result_without_discount[b] = max(result_without_discount[b], with_discount[b - full_cost] + profit)

            half_cost = present[u] >> 1
            for b in range(half_cost, budget + 1):
                profit = future[u] - half_cost
                result_with_discount[b] = max(result_with_discount[b], with_discount[b - half_cost] + profit)

            return result_without_discount, result_with_discount


        return max(dp(0, -1)[0])
