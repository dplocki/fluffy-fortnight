class Solution:
    MOD = 10**9 + 7

    def numberOfWays(self, corridor: str) -> int:
        result = 1
        seats = 0
        last_seat = None

        for index, c in enumerate(corridor):
            if c != 'S':
                continue

            if seats == 2:
                result = (result * (index - last_seat)) % Solution.MOD
                seats = 0

            seats += 1
            last_seat = index

        if seats != 2:
            return 0

        return result % Solution.MOD
