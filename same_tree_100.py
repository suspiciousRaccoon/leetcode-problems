class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p and q:
            return all((p.val == q.val, self.isSameTree(q.left, p.left), self.isSameTree(q.right, p.right)))
        return p is q
