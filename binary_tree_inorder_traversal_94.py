from typing import List
from utils import TreeNode


class Solution:
    def recursive_inorder_traversal(self, root: None | TreeNode) -> List[int]:
        result = []

        def in_order(root):
            if not root:
                return None
            in_order(root.left)
            result.append(root.val)
            in_order(root.right)
        in_order(root)
        return result

    def iterative_inorder_traversal(self, root: None | TreeNode) -> List[int]:
        """
        Does the same as the recursive approach but with a stack.
        We append the value to the stack, then traverse the left branch.
        We append the leaf to the result and and start the process again with the right child

        For 
            1
          /   \
         2     3
        / \   /  \
       4   5  6   7

       stack:
       [1, 2, 4] -> [1, 2] -> [1, 5] -> [1]       -> [1, 3, 6] -> [1, 3]
       result:
       [       ] -> [4   ] -> [4, 2] -> [4, 2, 5] -> [4, 2, 5] -> [4, 2, 5, 6]
        """
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
