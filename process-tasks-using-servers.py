NEW_TASK, FINISH_TASK = 1, 0

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        result = [0] * len(tasks)

        events_queue = [(r, NEW_TASK, r) for r in range(len(tasks))]
        heapify(events_queue)

        waiting_task = []

        free_servers_queue = [(w, i) for i, w in enumerate(servers)]
        heapify(free_servers_queue)

        while events_queue:
            timestamp, event_type, task_index = heappop(events_queue)

            if event_type == NEW_TASK:
                heappush(waiting_task, task_index)
            else:
                server_index = result[task_index]
                heappush(free_servers_queue, (servers[server_index], server_index))

            if events_queue and events_queue[0][0] == timestamp:
                continue

            while waiting_task and free_servers_queue:
                task_id = heappop(waiting_task)
                _, server_id = heappop(free_servers_queue)
                heappush(events_queue, (timestamp + tasks[task_id], FINISH_TASK, task_id))
                result[task_id] = server_id

        return result
