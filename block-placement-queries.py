from sortedcontainers import SortedList


class Node:
    def __init__(self, n: int):
        self.n = 1 << n.bit_length()
        self.tree = [0] * (self.n << 1)

    def update(self, x: int, value: int):
        x += self.n
        self.tree[x] = value
        while x > 1:
            x //= 2
            self.tree[x] = max(self.tree[x << 1], self.tree[(x << 1) + 1])
    
    def check(self, x: int) -> int:
        x += self.n
        res = self.tree[x]
        while x > 1:
            if x & 1:
                res = max(res, self.tree[x - 1])

            x //= 2
        return res

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        axis = SortedList()
        tree = Node(max(q[1] for q in queries))

        axis.add(0)
        tree.update(0,0)

        result = []
        for query in queries:
            if query[0] == 1:
                ind = axis.bisect(query[1])
                if ind < len(axis):
                    nxt = axis[ind]
                    tree.update(nxt, nxt - query[1])

                tree.update(query[1], query[1] - axis[ind-1])
                axis.add(query[1])
            else:
                previous = axis[axis.bisect(query[1]) - 1]
                maxium = max(query[1] - previous, tree.check(previous))

                result.append(query[2] <= maxium)

        return result
