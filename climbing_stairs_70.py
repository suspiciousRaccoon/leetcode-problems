"""
Works like the fibonacci sequence
1 step: -                                          (1)
2 step: - - or =                                   (2)
3 step: - - - or = - or = -                        (3)
4 step: - - - - or - - = or = - - or - = - or = =  (5)

we can look at the nth number of steps as a sum of a smaller number of steps.
for 4 steps, we are combining the possibilities of 1 steps with 3 steps, 1 steps with 2 steps, and simply 2 steps
if we look at all the possibilities within each number of steps and sum them, we can see that
the nth step will have the possibilities of (n-1) + (n-2) = 3 step + 2 step = 5 total steps
which is the fibonacci sequence
"""


class Solution:  # dynamic programming!!!!!
    def climbStairs(self, n: int) -> int:
        value1 = 1
        value2 = 1
        for i in range(n):
            value1, value2 = value1 + value2, value1
        return value1


# Exceeds time limit :C
class RecursiveSolution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
