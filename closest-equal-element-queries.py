class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        n2 = n << 1
        miniaml_distances = [n2] * n2

        last_value = {}
        for index in range(n2):
            current = nums[index % n]

            if current in last_value:
                miniaml_distances[index] = min(miniaml_distances[index], index - last_value[current])

            last_value[current] = index

        last_value = {}
        for index in range(n2, -1, -1):
            current = nums[index % n]

            if current in last_value:
                miniaml_distances[index] = min(miniaml_distances[index], last_value[current] - index)

            last_value[current] = index

        result = []
        for query in queries:
            r = min(miniaml_distances[query], miniaml_distances[query + n])
            result.append(-1 if r >= n else r)

        return result
