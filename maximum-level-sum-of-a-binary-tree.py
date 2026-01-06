# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maximum_sum_of_level = root.val
        nodes = [root]
        level = 0
        result = 1

        while nodes:
            level += 1
            sum_on_level = 0
            new_nodes = []

            for node in nodes:
                sum_on_level += node.val
                if node.left:
                    new_nodes.append(node.left)

                if node.right:
                    new_nodes.append(node.right)
            
            nodes = new_nodes

            if sum_on_level > maximum_sum_of_level:
                result = level
                maximum_sum_of_level = sum_on_level

        return result
