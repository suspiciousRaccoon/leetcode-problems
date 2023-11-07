from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        """
        In this approach since we're sorting we don't care about the index of the monster, only their arrival time
        """
        current_time = 0
        arrival_times = sorted([(dist[i] / speed[i])
                               for i in range(len(dist))])
        for time in arrival_times:
            if time <= current_time:
                break
            current_time += 1
        return current_time
