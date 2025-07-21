# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        return list(self.zigzag(root))

    def zigzag(self, root: Optional[TreeNode]):
        left_to_right = True
        for line in self.traverse_tree(root):
            values = [node.val for node in line]
            if left_to_right:
                yield values
            else: 
                yield values[::-1]

            left_to_right = not left_to_right

    def traverse_tree(self, root: Optional[TreeNode]):
        line = [root]

        while line:
            yield line
            new_line = []
            for node in line:
                if node.left:
                    new_line.append(node.left)
                
                if node.right:
                    new_line.append(node.right)

            line = new_line
