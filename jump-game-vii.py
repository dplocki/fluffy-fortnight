class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        end = len(s) - 1
        to_check = deque([0])

        while to_check:
            start_index = to_check.popleft()
            if start_index == end:
                return True

            for j in range(start_index + minJump, start_index + maxJump + 1):
                if j > end:
                    break

                if s[j] != '0':
                    continue

                to_check.append(j)

        return False
