# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(left, right):
            if left > right:          # no elements → empty subtree
                return None
            
            mid = (left + right) // 2 # always pick lower-middle
            
            node = TreeNode(nums[mid])
            node.left  = build(left, mid - 1)   # left half
            node.right = build(mid + 1, right)  # right half
            
            return node
        
        return build(0, len(nums) - 1)
        