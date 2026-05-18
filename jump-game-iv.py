class Solution:
    def minJumps(self, arr: List[int]) -> int:
        jumps = {}
        for index, value in enumerate(arr):
            if value not in jumps:
                jumps[value] = []
            
            jumps[value].append(index)
        
        to_check = [(0, 0)]
        n = len(arr)
        results = {}

        while to_check:
            current_steps, current_index = heappop(to_check)
            if current_index == n - 1:
                return current_steps

            results[current_index] = current_steps

            if current_index > 0 and results.get(current_index - 1, n) > current_steps - 1:
                heappush(to_check, (current_steps + 1, current_index - 1))

            if current_index < n - 1 and results.get(current_index + 1, n) > current_steps + 1:
                heappush(to_check, (current_steps + 1, current_index + 1))

            new_steps = current_steps + 1
            for jump in jumps[arr[current_index]]:
                if jump == current_index:
                    continue

                if results.get(jump, n) > new_steps:
                    heappush(to_check, (new_steps, jump))
        
        raise Exception('that shouldn\'t be possible')
