class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        invoke = defaultdict(list)
        for a, b in invocations:
            invoke[a].append(b)

        to_remove = [False] * n
        to_remove[k] = True
        to_check = [k]
        while to_check:
            method = to_check.pop()

            for m in invoke[method]:
                if not to_remove[m]:
                    to_remove[m] = True
                    to_check.append(m)

        for a, b in invocations:
            if to_remove[b] and not to_remove[a]:
                return list(range(n))

        return [m for m in range(n) if not to_remove[m]]
