from dataclasses import dataclass, field

@dataclass
class Node:
    left_border: int
    right_border: int
    middle: int = field(default=None)
    left: Node = field(default=None)
    right: Node = field(default=None)

    def split(self, x: int) -> None:
        if self.middle == None:
            self.middle = x
            self.left = Node(self.left_border, x)
            self.right = Node(x, self.right_border)
            return

        if x < self.middle:
            self.left.split(x)
            return

        if x > self.middle:
            self.right.split(x)

    def check(self, x: int, size: int) -> bool:
        if self.middle == None:
            return min(self.right_border, x) - self.left_border >= size

        return self.left.check(x, size) or self.right.check(x, size) 


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        tree = Node(0, inf)
        result = []

        for query in queries:
            if query[0] == 1:
                tree.split(query[1])
            elif query[0] == 2:
                result.append(tree.check(query[1], query[2]))

        return result
