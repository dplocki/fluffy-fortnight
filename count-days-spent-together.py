MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        def parse(date: str) -> int:
            month, day = map(int, date.split('-'))
            return sum(MONTH_DAYS[:month - 1]) + day

        start = max(parse(arriveAlice), parse(arriveBob))
        end = min(parse(leaveAlice), parse(leaveBob))
        result = end - start + 1

        return 0 if result < 0 else result
