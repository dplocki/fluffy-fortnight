class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions = { id: height for id, height in restrictions }
        restrictions[1] = 0
        to_check, visited = [], set()
        heappush(to_check, (0, 1, 0))

        while to_check:
            negative_max_height, current_id, current_height = heappop(to_check)
            if (current_id, current_height) in visited:
                continue

            visited.add((current_id, current_height))

            next_id = current_id + 1
            if next_id > n:
                return -negative_max_height

            next_height = current_height + 1
            next_max_height = max(-negative_max_height, next_height)
            if next_height <= restrictions.get(next_id, inf) and (next_id, next_height) not in visited:
                heappush(to_check, (-next_max_height, next_id, next_height))

            next_height = current_height
            if 0 <= next_height <= restrictions.get(next_id, inf) and (next_id, next_height) not in visited:
                heappush(to_check, (negative_max_height, next_id, next_height))

            next_height = current_height - 1
            if 0 <= next_height <= restrictions.get(next_id, inf) and (next_id, next_height) not in visited:
                heappush(to_check, (negative_max_height, next_id, next_height))

        return 0
