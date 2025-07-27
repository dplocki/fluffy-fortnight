# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        first_left = root.left
        first_right = root.right
        last_left = self.flatten(first_left)
        last_right = self.flatten(first_right)
        
        prev = root
        prev.left = None
        if last_left:
            prev.right = first_left
            prev = last_left

        if last_right:
            prev.right = first_right
            prev = last_right

        return prev
