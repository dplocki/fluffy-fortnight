class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 30 # 360 / 12
        minut_angle = 6 # 360 / 60

        short_hand = hour_angle * (hour % 12) + ((minutes % 60) / 60) * hour_angle
        longer_hand = minut_angle * minutes

        return min(abs(short_hand - longer_hand), 360 + short_hand - longer_hand, 360 + longer_hand - short_hand)
