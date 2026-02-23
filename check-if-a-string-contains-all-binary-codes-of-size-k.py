class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set(Solution.sliding_window(s, k))) == 2 ** k

    def sliding_window(iterable, n):
        "Collect data into overlapping fixed-length chunks or blocks."
        iterator = iter(iterable)
        window = deque(islice(iterator, n - 1), maxlen=n)
        for x in iterator:
            window.append(x)
            yield tuple(window)
