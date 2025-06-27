# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def internal():
            line = deque([root])

            while line:
                yield line[-1].val
                new_line = deque()

                while line:
                    element = line.popleft()
                    if element.left:
                        new_line.append(element.left)

                    if element.right:
                        new_line.append(element.right)

                line = new_line

        if not root:
            return []

        return list(internal())
