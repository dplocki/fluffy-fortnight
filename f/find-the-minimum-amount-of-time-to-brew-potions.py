class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        finish_times = [0] * n

        for current in mana:
            work_times = [s * current for s in skill]
            current_start_time = 0
            cumulative_work = 0
            
            for i in range(n):
                current_start_time = max(current_start_time, finish_times[i] - cumulative_work)
                cumulative_work += work_times[i]

            cumulative_work = 0
            for i in range(n):
                cumulative_work += work_times[i]
                finish_times[i] = current_start_time + cumulative_work

        return finish_times[-1]
