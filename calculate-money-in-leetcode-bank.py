class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks_number, day_lefts = divmod(n, 7)
        return (28 * 2 + 7 * (full_weeks_number - 1)) * full_weeks_number // 2 \
            + (full_weeks_number * 2 + 1 + day_lefts) * day_lefts // 2

        return result
