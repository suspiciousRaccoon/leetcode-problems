"""
This file contains util functions to avoid repeating them in the problems
"""

from typing import Any, Iterable

# Linked lists


class ListNode:
    def __init__(self, val=0, nextValue=None):
        self.val = val
        self.next = nextValue


def convert_to_linked_list(iterable: Iterable[Any]):
    """
    Converts an iterable into a linked list and retursn it
    """
    current = dummy = ListNode(0)
    for element in iterable:
        current.next = ListNode(element)
        current = current.next
    return dummy.next
