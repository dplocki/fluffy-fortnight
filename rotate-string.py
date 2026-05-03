class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False

        for m in range(n):
            if all(s[i] == goal[(i + m) % n] for i in range(n)):
                return True

        return False
