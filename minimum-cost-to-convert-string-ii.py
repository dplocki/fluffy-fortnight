class Solution:
    INFINITY = float('inf')

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        nodes = set(original) | set(changed)
        costs = {}

        for node in nodes:
            costs[node, node] = 0

        for a, b, c in zip(original, changed, cost):
            costs[a, b] = min(c, costs.get((a, b), Solution.INFINITY))

        for b in nodes:
            for a in nodes:
                for c in nodes:
                    current_cost = costs.get((a, b), Solution.INFINITY) + costs.get((b, c), Solution.INFINITY)
                    if current_cost < costs.get((a, c), Solution.INFINITY):
                        costs[a, c] = current_cost

        nodes = {}
        for (a, b), c in costs.items():
            if a == b:
                continue

            if a not in nodes:
                nodes[a] = {}
                
            if b not in nodes[a]:
                nodes[a][b] = c

        visited = set()
        to_check = [(0, source)]
        heapify(to_check)

        while to_check:
            current_cost, current_string = heappop(to_check)
            if current_string in visited:
                continue
 
            if current_string == target:
                return current_cost

            visited.add(current_string)

            for a in nodes.keys():
                a_size = len(node)
                for index in self.find_all(current_string, a):
                    for b in nodes[a]:
                        heappush(to_check, ( 
                            current_cost + nodes[a][b],
                            current_string[:index] + b + current_string[index + a_size:]
                        ))
                    
        return -1

    def find_all(self, string: str, substring: str) -> Generator[int, None, None]:
        index = 0
        while True:
            index = string.find(substring, index)
            if index == -1:
                return

            yield index
            index += 1
