class Solution:
    EVENT_ADD = 0
    EVENT_SUB = 1
    EVENT_COUNT = 2

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        events = []
        for index, station in enumerate(stations):
            events.append((index - r, Solution.EVENT_ADD, station))
            events.append((index, Solution.EVENT_COUNT, station))
            events.append((index + r + 1, Solution.EVENT_SUB, station))
        
        events.sort()
        power_stations = [0] * n
        power = 0

        for index, operation, station in events:
            if operation == Solution.EVENT_ADD:
                power += station
            elif operation == Solution.EVENT_SUB:
                power -= station
            elif operation == Solution.EVENT_COUNT:
                power_stations[index] = power
    
        left, right = 0, 1 << 40
        while left < right:
            mid = (left + right + 1) >> 1
            if self.is_min_power_possible(mid, n, r, k, power_stations):
                left = mid
            else:
                right = mid - 1

        return left

    def is_min_power_possible(self, target_power: int, n: int, r: int, k: int, power_stations: List[int]) -> bool:
            power_difference = [0] * (n + 1)
            added_power = 0

            for index in range(n):
                added_power += power_difference[index]
                power_deficit = target_power - power_stations[index] - added_power 

                if power_deficit > 0:
                    if k < power_deficit:
                        return False

                    k -= power_deficit
                    right_position = min(index + r, n - 1)

                    start = max(0, right_position - r)
                    end = min(right_position + r, n - 1)
                    power_difference[start] += power_deficit
                    power_difference[end + 1] -= power_deficit
                    added_power += power_deficit

            return True
