class Solution:
    MOD = 10**9 + 7

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        common = set(self.all_possible_sizes(hFences, m)) & set(self.all_possible_sizes(vFences, n))
        if not common: 
            return -1

        return (max(common) ** 2) % Solution.MOD

    def all_possible_sizes(self, fences: List[int], last: int) -> Generator[int, None, None]:
        sizes = [end - start for start, end in pairwise(sorted([1, last] + fences))]
        len_sizes = len(sizes)
        for index_a in range(len_sizes):
            result = sizes[index_a]
            yield result

            for index_b in range(index_a + 1, len_sizes):
                result += sizes[index_b]
                yield result
