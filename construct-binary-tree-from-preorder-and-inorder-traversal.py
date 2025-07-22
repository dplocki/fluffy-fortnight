# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_values_provider = (node for node in preorder)

        def build_node(start, end) -> Optional[TreeNode]:
            if end - start == 0:
                return None

            node_value = next(node_values_provider)
            node_value_index = find_index_in_range(inorder, node_value, start, end)

            return TreeNode(node_value,
                build_node(start, node_value_index),
                build_node(node_value_index + 1, end))

        def find_index_in_range(collection, target, start, end):
            return next((i for i in range(start, end) if collection[i] == target))

        return build_node(0, len(inorder))
