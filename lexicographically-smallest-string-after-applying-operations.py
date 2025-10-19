class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        result = tuple(ord(c) - ord('0') for c in s)
        to_check = [result]
        visited = set()
        
        while to_check:
            current = to_check.pop()
            if current in visited:
                continue

            if current < result:
                result = current

            visited.add(current)
            
            to_check.append(tuple(c if i % 2 == 0 else ((c + a) % 10) for i, c in enumerate(current)))
            to_check.append(current[-b:] + current[:-b])

        return ''.join(map(str, result))
