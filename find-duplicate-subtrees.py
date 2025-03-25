# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = {}
        library = set()

        _, library, result = self.serializeSubTree(library, result, root.left)
        _, library, result = self.serializeSubTree(library, result, root.right)

        return result.values()
    
    def serializeSubTree(self, library, duplicated_roots, root: Optional[TreeNode]):
        result = None
        if root == None:
            result = '_'
        else:
            result_left, library, duplicated_roots = self.serializeSubTree(library, duplicated_roots, root.left)
            result_right, library, duplicated_roots = self.serializeSubTree(library, duplicated_roots, root.right)

            result = f'{root.val} {result_left} {result_right}'
        
            if result in library:
                duplicated_roots[result] = root
            else:
                library.add(result)

        return result, library, duplicated_roots
