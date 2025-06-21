# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return self.deep(root, 1)

    def deep(self, root, current_deep_level: int) -> int:
        if root.left == None and root.right == None:
            return current_deep_level

        if root.left == None:
            return self.deep(root.right, current_deep_level + 1)

        if root.right == None:
            return self.deep(root.left, current_deep_level + 1)

        return max(
            self.deep(root.left, current_deep_level + 1),
            self.deep(root.right, current_deep_level + 1))
