# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        result_line = []
        lines = deque([[root]])
        new_line = []

        while lines:
            line = lines.popleft()
            for node in line:
                result_line.append(node.val)
                if node.left:
                    new_line.append(node.left)

                if node.right:
                    new_line.append(node.right)

            if result_line:
                result.append(result_line)
                result_line = []

            if new_line:
                lines.append(new_line)
                new_line = []

        return result
