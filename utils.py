"""
This file contains util functions to avoid repeating them in the problems
"""

from typing import Any, Iterable, List

# Linked lists


class ListNode:
    def __init__(self, val: Any, next_value: Any | None = None) -> None:
        self.val = val
        self.next = next_value


def convert_to_linked_list(iterable: Iterable[Any]) -> ListNode:
    """
    Converts an iterable into a linked list and returns it
    """
    current = dummy = ListNode(0)
    for element in iterable:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# binary search


def binary_search_recursion(arr: List[int], target: int, left: int, right: int) -> int:
    """
    Looks for an integer in a list via bynary search and recursion. return -1 if not found
    """
    if left <= right:

        middle = (right + left) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            return binary_search(arr, left, middle - 1, target)
        else:
            return binary_search(arr, middle + 1, right, target)
    else:
        return -1


def binary_search(arr: List[int], target: int) -> int:
    """
    Looks for an integer in a list via bynary search. return -1 if not found
    """
    left = 0
    right = len(arr) - 1
    middle = 0

    while left <= right:
        middle = (right + left) // 2

        if arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1
        else:
            return middle

    return -1
