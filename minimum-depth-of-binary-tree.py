# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        nodes_to_check = deque([])
        nodes_to_check.append((1, root))

        while nodes_to_check:
            depth, node = nodes_to_check.popleft()

            if node.left == None and node.right == None:
                return depth

            if node.left:
                nodes_to_check.append((depth + 1, node.left))

            if node.right:
                nodes_to_check.append((depth + 1, node.right))
