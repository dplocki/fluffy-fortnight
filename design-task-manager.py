class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks_db = {}
        self.task_priorities = []
        self.removed_tasks = set() 

        for task in tasks:
            self.add(*task)

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        self.tasks_db[task_id] = (user_id, priority)
        heappush(self.task_priorities, (-priority, -task_id))

    def edit(self, task_id: int, new_priority: int) -> None:
        user_id, old_priority = self.tasks_db[task_id]
        self.removed_tasks.add((-old_priority, -task_id))
        self.tasks_db[task_id] = (user_id, new_priority)
        heappush(self.task_priorities, (-new_priority, -task_id))

    def rmv(self, task_id: int) -> None:
        user_id, old_priority = self.tasks_db[task_id]
        del self.tasks_db[task_id]
        self.removed_tasks.add((-old_priority, -task_id))

    def execTop(self) -> int:
        while self.task_priorities:
            priority, task_id = self.task_priorities[0]
            
            if (priority, task_id) in self.removed_tasks:
                heappop(self.task_priorities)
                self.removed_tasks.remove((priority, task_id))
                continue
            
            actual_task_id = -task_id
            if actual_task_id not in self.tasks_db:
                heappop(self.task_priorities)
                continue

            heappop(self.task_priorities)
            executed_task_id = actual_task_id
            user_id, _ = self.tasks_db[executed_task_id]
            del self.tasks_db[executed_task_id]
            return user_id
        
        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
