class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        children = {}
        for n, p in enumerate(parent):
            if n not in children:
                children[n] = []

            if p not in children:
                children[p] = []
            
            children[p].append(n)

        result = [1] * len(s)
        letter_node = {}


        def backtrack(node: int) -> None:
            letter = s[node]
            new_parent = letter_node.get(letter, -1)
            letter_node[letter] = node

            for child in children[node]:
                backtrack(child)

            letter_node[letter] = new_parent
            if not node:
                return
        
            result[new_parent if new_parent != -1 else parent[node]] += result[node]


        backtrack(0)
        return result
