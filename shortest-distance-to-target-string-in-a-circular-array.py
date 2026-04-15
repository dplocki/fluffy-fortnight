class Solution:
    def closestTarget(self, words: List[str], target: str, start_index: int) -> int:
        n = len(words)
        steps = 0

        while steps < n:
            if words[(start_index + steps) % n] == target or words[(start_index - steps) % n] == target:
                return steps

            steps += 1

        return -1
