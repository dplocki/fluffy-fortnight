class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        max_candidates = len(candidates)

        def internal(target, start_index, current):
            if target == 0:
                yield tuple(current)
                return

            for index in range(start_index, max_candidates):
                candidate = candidates[index]

                current.append(candidate)
                yield from internal(target - candidate, index + 1, current)
                current.pop()

        candidates.sort()
        return list(set(internal(target, 0, [])))
