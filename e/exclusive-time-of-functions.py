class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * (n + 1)
        stack = [n]
        prev_time = 0
        logs = iter(map(lambda l: (int(l[0]), l[1], int(l[2])), map(lambda l: l.split(':'), logs)))
        for id, name, time in logs:
            current_process = stack.pop()
            result[current_process] += time - prev_time

            if name == 'start':
                result[current_process] -= 1
                stack.append(current_process)
                stack.append(id)
            elif name == 'end':
                result[current_process] += 1

            prev_time = time

        return result[:-1]
