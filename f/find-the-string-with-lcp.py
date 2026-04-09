class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        result = [None] * n

        result_index = 0
        for letter in string.ascii_lowercase:
            while result_index < n and result[result_index] != None:
                result_index += 1

            if result_index == n:
                break

            for i in range(result_index, n):
                if lcp[result_index][i] > 0:
                    result[i] = letter

        if None in result:
            return ''

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if result[i] == result[j]:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            return ''
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ''
                else:
                    if lcp[i][j] != 0:
                        return ''

        return ''.join(result)
