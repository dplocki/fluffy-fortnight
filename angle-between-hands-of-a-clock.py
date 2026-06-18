class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        short_hand = (360 / 12) * (hour % 12) + (360 / 12) * ((minutes % 60) / 60)
        longer_hand = (360 / 60) * minutes

        return abs(short_hand - longer_hand)
