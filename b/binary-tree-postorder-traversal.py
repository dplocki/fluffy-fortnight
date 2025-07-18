# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional
[TreeNode]) -> List[int]:
        return list(self.preorder_traversal(root))

    def preorder_traversal(self, root: Optional[TreeNode]):
        if not root:
            return
        
        yield from self.preorder_traversal(root.left)
        yield from self.preorder_traversal(root.right)
        yield root.val
