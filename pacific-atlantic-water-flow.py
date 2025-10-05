class Solution:
    DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])

        def find_flows(to_check: List[int]):
            result = set()

            while to_check:
                r, c = to_check.pop()
                if (r,c) in result:
                    continue

                result.add((r, c))
                for rd, cd in Solution.DIRS:
                    nr = r + rd
                    nc = c + cd

                    if nr < 0 or nr > rows - 1 or nc < 0 or nc > columns - 1:
                        continue

                    print(nr, nc, '-', r, c, '|', rows, columns)
                    if heights[nr][nc] >= heights[r][c]:
                        to_check.append((nr, nc))

            return result

        to_atlantic = find_flows(
            list(chain(
                ((0, i) for i in range(columns)),
                ((i, 0) for i in range(rows)))))

        to_pacific = find_flows(
            list(chain(
                ((rows - 1, i) for i in range(columns)),
                ((i, columns - 1) for i in range(rows)))))

        return list(to_atlantic & to_pacific)
