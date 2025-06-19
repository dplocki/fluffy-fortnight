# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def interal(root: Optional[TreeNode], from_top: str) -> int:
            new_from_top = from_top + str(root.val) 

            if not root.left and not root.right:
                return int(new_from_top)

            result = 0
            if root.left:
                result += interal(root.left, new_from_top)

            if root.right:
                result += interal(root.right, new_from_top)

            return result

        return interal(root, '')
