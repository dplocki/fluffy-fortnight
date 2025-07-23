# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        nodes_number = len(postorder)

        def find_from_index(collection: List[int], target: int, start: int):
            return next((i for i in range(start, nodes_number) if collection[i] == target), None)

        def build_node(start: int) ->  Optional[TreeNode]:
            if not postorder:
                return None

            root_value = postorder[-1]
            index = find_from_index(inorder, root_value, start)
            if index == None:
                return None
            
            value = postorder.pop()
            right_node = build_node(index)

            return TreeNode(
                root_value,
                build_node(start),
                right_node
            )

        return build_node(0)
