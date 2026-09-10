# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:


        def interal(node: TreeNode) -> int:
            if not node:
                return 0, 0, 0

            left_result, left_sum, left_count = interal(node.left)
            right_result, right_sum, right_count = interal(node.right)

            node_sum = left_sum + right_sum + node.val
            node_count = left_count + right_count + 1
            result = left_result + right_result

            if node_sum // node_count == node.val:
                result += 1

            return result, node_sum, node_count
        

        return interal(root)[0]
