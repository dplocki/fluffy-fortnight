class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = list(map(sub, startTime + [eventTime], [0] + endTime))

        result = current_gap = 0
        for index, x in enumerate(gaps):
            current_gap += x
            if index >= k:
                result = max(result, current_gap)
                current_gap -= gaps[index - k]

        return result
