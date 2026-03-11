# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return sum(Solution.find_all_numbers_in_tree(root, 0))

    def find_all_numbers_in_tree(node: Optional[TreeNode], above_value: int) -> Generator[int, None, None]:
        if node == None:
            return

        new_value = (above_value << 1) + node.val
        if not node.left and not node.right:
            yield new_value
            return

        yield from Solution.find_all_numbers_in_tree(node.left, new_value)
        yield from Solution.find_all_numbers_in_tree(node.right, new_value)
  
