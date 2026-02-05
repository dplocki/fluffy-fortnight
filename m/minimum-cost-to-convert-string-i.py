class Solution:
    INFINITY = float('inf')

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        letters = set(original) | set(changed)
        transfer = {}

        for letter in letters:
            transfer[letter, letter] = 0

        for a, b, c in zip(original, changed, cost):
            transfer[a, b] = min(c, transfer.get((a, b), Solution.INFINITY))

        for b in letters:
            for a in letters:
                for c in letters:
                    cost = transfer.get((a, b), Solution.INFINITY) + transfer.get((b, c), Solution.INFINITY)
                    if cost < transfer.get((a, c), Solution.INFINITY):
                        transfer[a, c] = cost

        result = 0
        for a, b in zip(source, target):
            if a == b:
                continue

            cost = transfer.get((a, b), None)
            if cost == None:
                return -1

            result += cost
        
        return result
