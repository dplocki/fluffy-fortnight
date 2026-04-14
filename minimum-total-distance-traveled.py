class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        robots = len(robot)
        factories = len(factory)

        @cache
        def internal(robot_index: int, factory_index: int) -> int:
            if robot_index == robots:
                return 0

            if factory_index == factories:
                return inf

            result = internal(robot_index, factory_index + 1)
            robots_moves = 0
            factory_position = factory[factory_index][0]

            for i in range(factory[factory_index][1]):
                if robot_index + i >= robots:
                    break

                robots_moves += abs(robot[robot_index + i] - factory_position)

                result = min(
                    result,
                    robots_moves + internal(robot_index + i + 1, factory_index + 1)
                )

            return result

        return internal(0, 0)
