class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        event_times = []
        for start, end, value in events:
            event_times.append((start, True, value))
            event_times.append((end + 1, False, value))

        event_times.sort()

        max_result, current_max = 0, 0
        for _, is_event_start, value in event_times:
            if is_event_start:
                max_result = max(max_result, value + current_max)
            else:
                current_max = max(current_max, value)
    
        return max_result
