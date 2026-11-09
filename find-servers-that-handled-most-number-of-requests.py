class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        handled, busy = [], []

        for index, (task_begin, task_lenght) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= task_begin:
                heappush(available, index + (heappop(busy)[1] - index) % k)

            if available:
                id = heappop(available) % k
                heappush(busy, (task_begin + task_lenght, id))
                handled.append(id)

        return multimode(handled)
