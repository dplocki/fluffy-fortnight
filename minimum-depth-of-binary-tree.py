# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.find_minium(root, 0)

    def find_minium(self, node, current) -> int:
        if node == None:
            return 0

        if node.left == None and node.right == None:
            return current + 1

        left = self.find_minium(node.left, current + 1) if node.left != None else None
        right = self.find_minium(node.right, current + 1) if node.right != None else None

        if left == None:
            return right
        elif right == None:
            return left
        
        return min(left, right)

