# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root == None:
            return result

        line = [root]
        while line:
            new_line = []
            result_line = []
            for node in line:
                result_line.append(node.val)
                if node.left:
                    new_line.append(node.left)
                if node.right:
                    new_line.append(node.right)

            result.append(result_line)
            line = new_line

        return result[::-1]
