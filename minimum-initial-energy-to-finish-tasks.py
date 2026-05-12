class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda a: a[1] - a[0], reverse=True)

        result = 0
        current = 0

        for actual, minimum in tasks:
            if current < minimum:
                result += minimum - current
                current = minimum

            current -= actual

        return result
