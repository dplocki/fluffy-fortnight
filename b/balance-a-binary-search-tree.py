# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def traverse_tree(root):
            if root == None:
                return

            yield from traverse_tree(root.left)
            yield root.val
            yield from traverse_tree(root.right)

        def build_tree(nodes, start, end):
            if start > end:
                return None
                
            middle = (start + end) >> 1
            left = build_tree(nodes, start, middle - 1)
            right = build_tree(nodes, middle + 1, end)
            return TreeNode(nodes[middle], left, right)

        nodes = list(traverse_tree(root))
        return build_tree(nodes, 0, len(nodes) - 1)
