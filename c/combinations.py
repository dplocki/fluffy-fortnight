class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current = []

        def internal(number: int):
            current_size = len(current)
            if current_size == k:
                yield tuple(current)
                return
            elif current_size > k:
                return

            if number > n:
                return

            current.append(number)
            yield from internal(number + 1)
            current.pop()
            yield from internal(number + 1)

        return list(internal(1))
