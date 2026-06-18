class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mins = 6 * minutes
        hrs = 30 * hour + 0.5 * minutes
        first_angle = abs(hrs - mins)
        second_angle = 360 - first_angle 
        return min(first_angle,second_angle)
        