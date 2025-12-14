class Solution:
    MOD = 10**9 + 7

    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)

        def internal(start: int) -> int:
            seats = 0
            last_seat = None
            for index, c in enumerate(corridor[start:], start):
                if c != 'S':
                    continue

                if seats == 2:
                    return (index - last_seat) * internal(index)

                seats += 1
                last_seat = index

            return 1 if seats == 2 else 0

        return internal(0) % Solution.MOD
