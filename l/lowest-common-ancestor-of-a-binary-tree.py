# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root

        if not root or (not root.left and not root.right):
            return None

        left_part = self.lowestCommonAncestor(root.left, p, q)
        right_part = self.lowestCommonAncestor(root.right, p, q)
        if left_part == None:
            return right_part
        elif right_part == None:
            return left_part
        
        return root
