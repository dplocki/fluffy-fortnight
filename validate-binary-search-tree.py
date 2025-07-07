# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_binary_node(root, None, None)

    def is_valid_binary_node(self, node, minimum, maximum) -> bool:
        if not node:
            return True

        if (minimum and node.val <= minimum) or (maximum and node.val >= maximum):
            return False

        if node.left and (node.left.val > node.val or not self.is_valid_binary_node(node.left, minimum, node.val)):
            return False

        if node.right and (node.right.val < node.val or not self.is_valid_binary_node(node.right, node.val, maximum)):
            return False

        return True
