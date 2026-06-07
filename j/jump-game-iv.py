class Solution:
    def minJumps(self, arr: List[int]) -> int:
        jumps = {}
        for index, value in enumerate(arr):
            if value not in jumps:
                jumps[value] = []
            
            jumps[value].append(index)

        for indexes in jumps.values():
            indexes.sort(reverse=True)
        
        to_check = deque([(0, 0)])
        n = len(arr)
        visited = set()

        while to_check:
            current_steps, current_index = to_check.popleft()
            if current_index == n - 1:
                return current_steps

            visited.add(current_index)

            next_index = current_index - 1
            if next_index >= 0 and (next_index not in visited):
                if next_index == n - 1:
                    return current_steps + 1
                visited.add(next_index)
                to_check.append((current_steps + 1, next_index))

            next_index = current_index + 1
            if next_index < n and (next_index not in visited):
                visited.add(next_index)
                to_check.append((current_steps + 1, next_index))

            new_steps = current_steps + 1
            for next_index in jumps[arr[current_index]]:
                if next_index == current_index:
                    continue

                if next_index == n - 1:
                    return new_steps

                if next_index not in visited:
                    visited.add(next_index)
                    to_check.append((new_steps, next_index))

            jumps[arr[current_index]] = []
        
        raise Exception('that shouldn\'t be possible')
