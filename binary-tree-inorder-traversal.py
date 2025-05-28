# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def inorder_traversal(root: Optional[TreeNode]):
            if root == None:
                return

            if root.left:
                yield from inorder_traversal(root.left)

            yield root.val

            if root.right:
                yield from inorder_traversal(root.right)

        return list(inorder_traversal(root))
