# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.calculate_hight(root) >= 0

    def calculate_hight(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return 0

        left = self.calculate_hight(root.left)
        right = self.calculate_hight(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return 1 + max(left, right)
