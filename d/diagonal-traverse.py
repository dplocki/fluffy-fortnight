class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        return list(self.diagonal_traverse(mat))

    def diagonal_traverse(self, mat):
        m = len(mat)
        n = len(mat[0])
        r, c = 0, 0
       
        while 0 <= r < m and 0 <= c < n:
            while 0 <= r < m and 0 <= c < n:
                yield mat[r][c]
                r -= 1
                c += 1

            if c < n:
                r = 0
            else:
                c -= 1
                r += 2

            while 0 <= r < m and 0 <= c < n:
                yield mat[r][c]
                r += 1
                c -= 1

            if r < m:
                c = 0
            else:
                c += 2
                r = m - 1
