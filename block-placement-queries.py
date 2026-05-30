class Node:
    left_border: int
    right_border: int
    max_fit: int
    middle: int = None
    left: Node = None
    right: Node = None
    parent: Node = None

    def __init__(self, left: int, right: int, parent: None):
        self.left_border = left
        self.right_border = right
        self.max_fit = right - left
        self.parent = parent
    
    def split(self, x: int) -> None:
        if self.middle is None:
            self.middle = x
            self.left = Node(self.left_border, x, self)
            self.right = Node(x, self.right_border, self)
            self.max_fit = max(self.left.max_fit, self.right.max_fit)

            tmp = self.parent
            while tmp:
                new_fit = max(tmp.left.max_fit, tmp.right.max_fit)
                if new_fit == tmp.max_fit:
                    break
                tmp.max_fit = new_fit
                tmp = tmp.parent

            return

        if x < self.middle:
            self.left.split(x)
            return

        if x > self.middle:
            self.right.split(x)

    def check(self, x: int, size: int) -> bool:
        if self.middle == None:
            return min(self.right_border, x) - self.left_border >= size

        if x < self.middle:
            return self.left.check(x, size)

        return self.left.max_fit >= size or self.right.check(x, size)


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        tree = Node(0, inf, None)
        result = []

        for query in queries:
            if query[0] == 1:
                tree.split(query[1])
            elif query[0] == 2:
                result.append(tree.check(query[1], query[2]))

        return result
