class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(map(int, sorted(map(str, list(range(1, n + 1))))))
