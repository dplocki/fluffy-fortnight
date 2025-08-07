# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        paths = set()

        def internal(root):
            left = internal(root.left) if root.left else 0
            right = internal(root.right) if root.right else 0

            paths.add(left + root.val + right)
            maxium = max(root.val, left + root.val, root.val + right)
            paths.add(maxium)
            return maxium

        internal(root)
        return max(paths)
