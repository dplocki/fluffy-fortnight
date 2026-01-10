# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    MOD = 10**9 + 7

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sums = []

        def internal(node):
            if not node:
                return 0
            
            subtree_sum = internal(node.left) + node.val + internal(node.right)
            subtree_sums.append(subtree_sum)
            return subtree_sum
        
        total_sum = internal(root)
        return max(s * (total_sum - s) for s in subtree_sums) % Solution.MOD
