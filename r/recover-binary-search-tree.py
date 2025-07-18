# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        previous = swap_1 = swap_2 = None

        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return

            nonlocal previous, swap_1, swap_2

            traverse(node.left)

            if previous and previous.val > node.val:
                if swap_1 is None:
                    swap_1 = previous
                swap_2 = node

            previous = node
            traverse(node.right)

        traverse(root)
        swap_1.val, swap_2.val = swap_2.val, swap_1.val
