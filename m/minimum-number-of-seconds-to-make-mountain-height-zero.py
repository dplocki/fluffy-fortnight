class Solution:
    MAX = 10**16

    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        left, right = 1, Solution.MAX
        result = -1

        while left <= right:
            midle = (left + right) >> 1
            
            total_time = sum(
                int(sqrt((midle << 1) / worker_time + 0.25) - 0.5)
                for worker_time in workerTimes
            )

            if total_time >= mountainHeight:
                result = midle
                right = midle - 1
            else:
                left = midle + 1

        return result
