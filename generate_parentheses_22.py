"""
In this problem we explore all possible cases with a tree via recursion. 
We have a base case that exits the function once all possibilities are accounted for
and 2 other cases:
1st case: left parentheses is less than total number of parentheses pairs. 
2nd case: we have more left parentheses than right ones, thus being able to append
ending parentheses.
Once a possibility is ends it's recursion path we append it to results and exit the function

"""


class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def recursion(left, right, par):

            if left == right == n:
                result.append(par)
                return

            if left < n:
                recursion(left + 1, right, par+'(')

            if left > right:
                recursion(left, right + 1, par+')')

        recursion(0, 0, '')
        return result
