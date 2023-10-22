from typing import List


class Solution:
    """
    In this solution we iterate backwards and have a right_max variable to know if there will be a warmer day.
    If there won't, we simply ignore the result and update right_max.
    If there will, we check the number of days it'll take to have a warmer day.
    To do this we check the temperature to the right, and how many days it'll take for this temperature to have a warmer day and sum them.
    [73,74,75,71,69,72,76,73]

    [1 ,1 ,4 ,2 ,1 ,1 ,0 ,0 ]
              ^ we do 1 + 1 here
            ^ we do 1 + 2 + 1 here   
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length, right_max = len(temperatures), float('-inf')
        answer = [0] * length
        for index in range(length-1, -1, -1):  # we iterate backwards
            if right_max <= temperatures[index]:
                right_max = temperatures[index]
            else:
                days = 1
                while temperatures[index] >= temperatures[index + days]:
                    days += answer[index+days]
                answer[index] = days
        return answer


# O(n^2) solution, it exceeds time limit
class LongSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            counter = 0
            for j in range(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    answer[i] = counter
                    break
                counter += 1
        return answer
