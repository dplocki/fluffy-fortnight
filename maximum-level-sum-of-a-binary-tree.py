# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        def internal(root: Optional[TreeNode], level: int):
            if root == None:
                return

            yield (level, root.val)
            yield from internal(root.left, level + 1)
            yield from internal(root.right, level + 1)

        limit = 0
        dp = {}
        for level, value in internal(root, 1):
            dp[level] = dp.get(level, 0) + value
            limit = max(limit, level)

        maximum = max(dp.values())
        for level in range(1, limit + 1):
            if dp[level] == maximum:
                return level
