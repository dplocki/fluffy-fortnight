class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        minimum_distance = float('inf')
        for a, b in combinations(sorted(arr), 2):
            distance = b - a
            if distance < minimum_distance:
                result = []
                minimum_distance = distance

            if distance == minimum_distance:
                result.append((a, b))

        return result
