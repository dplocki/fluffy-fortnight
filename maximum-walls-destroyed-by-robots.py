class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        robot_with_distances = sorted(zip(robots, distance), key=lambda x: x[0])
        walls.sort()
      
        @cache
        def internal(robot_index: int, prev_robot_moved_right: int) -> int:
            if robot_index < 0:
                return 0
          
            current_positon, current_distance = robot_with_distances[robot_index]          
            left_boundary = current_positon - current_distance
          
            if robot_index > 0:
                left_boundary = max(left_boundary, robot_with_distances[robot_index - 1][0] + 1)
          
            left_wall_index = bisect_left(walls, left_boundary)
            right_wall_index = bisect_left(walls, current_positon + 1)
            walls_covered_left = internal(robot_index - 1, 0) + right_wall_index - left_wall_index
          
            right_boundary = current_positon + current_distance
          
            if robot_index + 1 < n:
                next_position, next_distance = robot_with_distances[robot_index + 1]
              
                if prev_robot_moved_right == 0:
                    right_boundary = min(right_boundary, next_position - next_distance - 1)
                else:
                    right_boundary = min(right_boundary, next_position - 1)
          
            left_wall_index = bisect_left(walls, current_positon)
            right_wall_index = bisect_left(walls, right_boundary + 1)
            walls_covered_right = internal(robot_index - 1, 1) + right_wall_index - left_wall_index
          
            return max(walls_covered_left, walls_covered_right)
      
        return internal(n - 1, 1)
