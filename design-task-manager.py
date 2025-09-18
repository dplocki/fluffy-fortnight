class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks_db = {}
        self.task_priorities = []

        for task in tasks:
            self.add(*task)

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        self.tasks_db[task_id] = (user_id, priority)
        heappush(self.task_priorities, (-priority, -task_id))

    def edit(self, task_id: int, new_priority: int) -> None:
        user_id, old_priority = self.tasks_db[task_id]
        self.tasks_db[task_id] = (user_id, new_priority)
        heappush(self.task_priorities, (-new_priority, -task_id))

    def rmv(self, task_id: int) -> None:
        del self.tasks_db[task_id]

    def execTop(self) -> int:
        while self.task_priorities:
            priority, neg_task_id = heappop(self.task_priorities)
            task_id = -neg_task_id

            if task_id not in self.tasks_db:
                continue

            user_id, current_priority = self.tasks_db[task_id]
            if -priority == current_priority:
                del self.tasks_db[task_id]
                return user_id

        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
