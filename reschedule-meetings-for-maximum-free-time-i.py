class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [startTime[0]]
        for i in range(1, len(endTime)):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        result = current_gap = 0
        for index, x in enumerate(gaps):
            current_gap += x
            if index >= k:
                result = max(result, current_gap)
                current_gap -= gaps[index - k]

        return result
