class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowed_swaps: List[List[int]]) -> int:
        subgraphs = list(range(len(source)))
        
        def get_subgraph(index: int) -> int:
            if subgraphs[index] != index:
                subgraphs[index] = get_subgraph(subgraphs[index])

            return subgraphs[index]

        for a, b in allowed_swaps:
            subgraphs[get_subgraph(a)] = get_subgraph(b)

        counters = {}
        for index, value in enumerate(source):
            subgraph_id = get_subgraph(index)
            
            if subgraph_id not in counters:
                counters[subgraph_id] = Counter()

            counters[subgraph_id][value] += 1

        result = 0
        for index, value in enumerate(target):
            subgraph_id = get_subgraph(index)

            counters[subgraph_id][value] -= 1
            if counters[subgraph_id][value] < 0:
                result += 1

        return result
