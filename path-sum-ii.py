# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def internal(node, target, path):
            if node == None:
                return

            new_target = target - node.val
            path.append(node.val)
            try:
                if not node.left and not node.right:
                    if new_target == 0:
                        yield tuple(path)
        
                    return

                yield from internal(node.left, new_target, path)
                yield from internal(node.right, new_target, path)
            finally:
                path.pop()

        return list(internal(root, targetSum, []))
