class Solution:
    END, OPEN = range(2)

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meeting_ending = { start: end for start, end in meetings }
        events = [ (me, Solution.OPEN, None) for me in meeting_ending.keys() ]
        heapq.heapify(events)
        room_count = {}
        available = [True] * (n + 1)
        waiting_line = deque()

        while events:
            timestamp, event_type, room = heapq.heappop(events)

            if event_type == Solution.OPEN:

                first_available = available.index(True)
                if first_available != n:
                    available[first_available] = False
                    room_count[first_available] = room_count.get(first_available, 0) + 1
                    heapq.heappush(events, (meeting_ending[timestamp], Solution.END, first_available))
                else:
                    waiting_line.append(timestamp)

            elif event_type == Solution.END:

                available[room] = True
                if waiting_line:
                    start = waiting_line.popleft()
                    available[room] = False
                    room_count[room] = room_count.get(room, 0) + 1
                    heapq.heappush(events, (meeting_ending[start] + timestamp - start, Solution.END, room))

            else:
                raise Exception('unknown event')

        return max(room_count, key=room_count.get)
