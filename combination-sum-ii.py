class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        max_candidates = len(candidates)
        current = []

        def internal(target, start_index):
            if target == 0:
                yield tuple(current)
                return
            
            if target < 0:
                return

            for index in range(start_index, max_candidates):
                candidate = candidates[index]
    
                if index > start_index and candidate == candidates[index - 1]:
                    continue

                current.append(candidate)
                yield from internal(target - candidate, index + 1)
                current.pop()

        candidates.sort()
        return list(internal(target, 0))
