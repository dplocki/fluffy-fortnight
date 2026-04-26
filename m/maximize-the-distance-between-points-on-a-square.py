class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        distances = [
            y if x == 0 else (side + x if y == side else (side * 3 - y if x == side else side * 4 - x))
            for x, y in points
        ]
        distances.sort()
        
        def check(limit: int) -> bool:
            perimeter = side * 4
            for start in distances:
                end = start + perimeter - limit
                current = start
                for _ in range(k - 1):
                    index = bisect_left(distances, current + limit)
                    if index == len(distances) or distances[index] > end:
                        current = -1
                        break

                    current = distances[index]

                if current >= 0:
                    return True

            return False


        left, right = 1, side
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
                result = mid
            else:
                right = mid - 1
                
        return result
