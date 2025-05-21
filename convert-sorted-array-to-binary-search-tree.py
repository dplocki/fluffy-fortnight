# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums: List[int], from_index: int, to_index: int) -> Optional[TreeNode]:
        if from_index > to_index:
            return None

        index = from_index + (to_index - from_index) // 2
        return TreeNode(
            nums[index],
            self.build_tree(nums, from_index, index - 1),
            self.build_tree(nums, index + 1, to_index)
        )
