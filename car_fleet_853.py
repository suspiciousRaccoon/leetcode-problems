from typing import List
"""
Instead of calculating the points at which cars intercept, we calculate the time they will take to
reach the target. To make sure they collide when we iterate, we sort the list and iterate backwards.
Each time there is a higher value for the time, we are sure that specific fleet won't collide.
"""


class Solution:
    def carFleet(self, target: int, positions: List[int], speed: List[int]) -> int:
        speeds = {positions[i]: speed[i] for i in range(len(positions))}
        positions.sort(reverse=True)
        fleets = 0
        prev_time = 0
        for pos in positions:
            time = (target-pos)/speeds[pos]
            if (time > prev_time):
                prev_time = time
                fleets += 1
        return fleets
