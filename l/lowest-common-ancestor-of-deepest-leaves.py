# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def internal(level: int, node: Optional[TreeNode]) -> Tuple[int, TreeNode]:
            if not node:
                return 0, None

            if not node.left and not node.right:
                return (level, node)

            left_deepest_level, left_node = internal(level + 1, node.left)
            right_deepest_level, right_node = internal(level + 1, node.right)

            if left_deepest_level == right_deepest_level:
                return left_deepest_level, node
            elif left_deepest_level > right_deepest_level:
                return left_deepest_level, left_node

            return right_deepest_level, right_node


        return internal(0, root)[1]
