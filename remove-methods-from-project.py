class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        not_affected = set(range(n))
        invoke = defaultdict(set)
        being_invoked = defaultdict(set)

        for a, b in invocations:
            invoke[a].add(b)
            being_invoked[b].add(a)

        result = set()
        to_check = [k]
        while to_check:
            method = to_check.pop()
            if method in result:
                continue

            result.add(method)
            not_affected.remove(method)
            to_check.extend(invoke[method] - result)

        if not not_affected:
            return []

        if all(not (being_invoked[method] - result) for method in result):
            return list(not_affected)

        return list(range(n))
