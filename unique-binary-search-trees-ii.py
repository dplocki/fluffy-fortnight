# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def internal(start: int, end: int):
            if start > end:
                yield None
                return

            for root_value in range(start, end + 1):
                right_trees = list(internal(root_value + 1, end))

                for left_subtree in internal(start, root_value - 1):
                    for right_subtree in right_trees:
                        yield TreeNode(root_value, left_subtree, right_subtree)

        return list(internal(1, n))
