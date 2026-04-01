class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        for current_robot, _ in sorted(enumerate(positions), key=lambda e: e[1]):
            if directions[current_robot] == 'R':
                stack.append(current_robot)
                continue

            while stack and healths[current_robot] > 0:
                going_right_robot = stack.pop()

                if healths[going_right_robot] > healths[current_robot]:
                    healths[going_right_robot] -= 1
                    healths[current_robot] = 0

                    stack.append(going_right_robot)
                elif healths[going_right_robot] < healths[current_robot]:
                    healths[going_right_robot] = 0
                    healths[current_robot] -= 1
                else:
                    healths[going_right_robot] = 0
                    healths[current_robot] = 0

        return [h for h in healths if h > 0]
