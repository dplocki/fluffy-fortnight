# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(root):
            if root == None:
                return

            yield from traverse(root.left)
            yield root.val
            yield from traverse(root.right)

        nodes = list(traverse(root))

        def build_tree(nodes, start, end):
            if start == end:
                return TreeNode(nodes[start])
            if start > end:
                return None
                
            middle = (start + end) >> 1
            left = build_tree(nodes, start, middle - 1)
            right = build_tree(nodes, middle + 1, end)
            return TreeNode(nodes[middle], left, right)
        
        return build_tree(nodes, 0, len(nodes) - 1)
