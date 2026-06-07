class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited, to_check = set(), [start]

        while to_check:
            current_index = to_check.pop()
            if current_index in visited:
                continue

            visited.add(current_index)

            current_value = arr[current_index]
            if current_value == 0:
                return True

            if current_index + current_value < n:
                to_check.append(current_index + current_value)
            
            if current_index - current_value >= 0:
                to_check.append(current_index - current_value)

        return False
