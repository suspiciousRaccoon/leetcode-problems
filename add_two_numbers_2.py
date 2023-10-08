"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional

from utils import convert_to_linked_list, ListNode


class Solution:

    def traverse_linked_list(self, list_node: ListNode) -> str:
        """
        Returns all values of a LinkedList as a string
        """
        return str(list_node.val) + (str(self.traverse_linked_list(list_node.next)) if list_node.next else "")

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value = int(self.traverse_linked_list(
            l1)[::-1]) + int(self.traverse_linked_list(l2)[::-1])
        return convert_to_linked_list([int(number) for number in str(value)[::-1]])


if __name__ == '__main__':
    solution = Solution()
    result = solution.add_two_numbers(convert_to_linked_list(
        [2, 4, 3]), convert_to_linked_list([5, 6, 4]))
    print(solution.traverse_linked_list(result))
