"""
This one was hard :c, had to look up the solution.

stolen explanation from leetcode:
Approach

    Initialize a variable maxArea to store the maximum area found, and a stack to keep track of the indices and heights of the histogram bars.

    Iterate through the histogram using an enumeration to access both the index and height of each bar.

    For each bar, calculate the width of the potential rectangle by subtracting the starting index (retrieved from the stack) from the current index.

    While the stack is not empty and the height of the current bar is less than the height of the bar at the top of the stack, pop elements from the stack to calculate the area of rectangles that can be formed.

    Update maxArea with the maximum of its current value and the area calculated in step 4.

    Push the current bar's index and height onto the stack to continue processing.

    After processing all bars, there may still be bars left in the stack. For each remaining bar in the stack, calculate the area using the height of the bar and the difference between the current index and the index at the top of the stack.

    Return maxArea as the result, which represents the largest rectangle area.

Complexity

    Time complexity: O(n), where n is the number of bars in the histogram. We process each bar once.
    Space complexity: O(n), as the stack can contain up to n elements in the worst case when the bars are in increasing order (monotonic).

//////////////////

The solution works with a monotonic stack that pops higher values when it encounters a lower element
It then calculates the possible areas of the popped elements via the indexes that are stored along with them.
The indexes (in the stack) aren't their place in the original list. They're the index of the start element that can support an area
Effectively, we have 2 indexes. The index of the start element that can support an area of h size, and the index of the current
element on the list

  x x
x x x x

In this case:
stack: [(0, 1), (1, 2), (1, 2), (0, 1)]
index: [   0       1       2       3  ]
We calculate an area when the height of the current element is lower than the height of the last element.
In this case, we calculate the height once we reach the 4th element on the heights list.

  x x
x x x x
      ^

last_height * (current_index - last_index)
2 * (3 - 1) = 4

Since we only do this when the height of the current element is lower, if we had a staircase we would never execute the code.

      x
    x x
  x x x
x x x x

stack: [(0, 1), (1, 2), (2, 3), (3, 4)]
index: [  0        1       2       3  ]
To compute these values, we take the length of the heights list instead.

current_height * (len(heights) - current_index
1 * (4 - 0) = 4
2 * (4 - 1) = 6
3 * (4 - 2) = 6
4 * (4 - 3) = 4
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # stores tuples (index, height)
        for current_index, current_height in enumerate(heights):
            start = current_index
            # checks if it's not empty and if the top value of the stack is greater than the current height
            while stack and stack[-1][1] > current_height:
                last_index, last_height = stack.pop()  # this unpacks the tuple into 2 variables
                # keep current area or assign new one.
                max_area = max(max_area, last_height *
                               (current_index - last_index))
                start = last_index
            stack.append((start, current_height))

        # calculate remaining areas in stack
        for current_index, current_height in enumerate(stack):
            max_area = max(max_area, current_height *
                           (len(heights) - current_index))
        return max_area
