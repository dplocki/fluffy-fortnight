class Solution:
    def countCollisions(self, directions: str) -> int:
        result = 0
        local_right = 0
        left_obstruction = False
        prev = None

        for direction in directions:

            if direction == 'L':
                if prev == 'R':
                    left_obstruction = True
                    result += local_right
                    local_right = 0

                if left_obstruction:
                    result += 1

            elif direction == 'R':
                local_right += 1

            elif direction == 'S':
                result += local_right
                local_right = 0
                left_obstruction = True

            prev = direction

        return result
