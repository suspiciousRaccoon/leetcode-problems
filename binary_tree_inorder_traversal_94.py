from typing import List
from utils import TreeNode


class Solution:
    def inorderTraversal(self, root: None | TreeNode) -> List[int]:
        result = []

        def in_order(root):
            if not root:
                return None
            in_order(root.left)
            result.append(root.val)
            in_order(root.right)
        in_order(root)
        return result
