class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])

        return all(
            row[(i + k) % n] == row[i]
            for row in mat
            for i in range(n))
