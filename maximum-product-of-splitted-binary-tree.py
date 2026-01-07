# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MOD = 10**9 + 7

    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def internal(root: Optional[TreeNode]) -> Generator[int, int, None]:
            if not root:
                return 0

            left = yield from internal(root.left)
            right = yield from internal(root.right)

            result = (left + root.val + right)
            yield result
            return result


        substries = list(internal(root))
        all_tree_size = substries.pop()

        return max(
            (all_tree_size - subtree_size) * subtree_size
            for subtree_size in substries) % Solution.MOD
