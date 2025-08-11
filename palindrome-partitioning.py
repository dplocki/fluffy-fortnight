class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s_length = len(s)
        is_palindrom = { (i, i):True for i in range(s_length) }

        for start in reversed(range(s_length)):
            for end in range(start + 1, s_length):
                is_palindrom[start, end] = s[start] == s[end] and is_palindrom.get((start + 1, end - 1), True)
        
        current_partitioning = []

        def internal(start: int):
            if start == s_length:
                yield tuple(current_partitioning)
                return

            for end in range(start, s_length):
                if not is_palindrom[start, end]:
                    continue

                current_partitioning.append(s[start:end + 1])
                yield from internal(end + 1)
                current_partitioning.pop()

        return list(internal(0))
