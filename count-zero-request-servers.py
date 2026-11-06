class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=itemgetter(1))
        result = [n] * len(queries)
        queries_order = sorted(range(len(queries)), key=lambda i: queries[i])
        server_activation = [0] * (n + 1)
        left, right = 0, 0
        active = 0

        for query_index in queries_order:
            query_time = queries[query_index]

            while right < len(logs) and logs[right][1] <= query_time:
                server_id = logs[right][0]
                if server_activation[server_id] == 0:
                    active += 1
                server_activation[server_id] += 1
                right += 1
                
            while left < right and logs[left][1] < query_time - x:
                server_id = logs[left][0]
                server_activation[server_id] -= 1
                if server_activation[server_id] == 0:
                    active -= 1
                left += 1

            result[query_index] = n - active

        return result
