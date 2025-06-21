# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.are_mirror(root.left, root.right)

    def are_mirror(self, left, right):
        if left == right:
            return True

        if (left == None or right == None) or (left.val != right.val):
            return False

        return self.are_mirror(left.left, right.right) and self.are_mirror(left.right, right.left)
