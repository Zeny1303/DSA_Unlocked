# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right) -> bool:
            if not left and not right:  # both None → symmetric
                return True
            if not left or not right:   # one None → not symmetric
                return False
            
            return (left.val == right.val and
                    isMirror(left.left, right.right) and   # outer pair
                    isMirror(left.right, right.left))      # inner pair
        
        return isMirror(root.left, root.right)
        