# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.ans = float('-inf')

        def dfs(node):

            if not node:
                return 0

            # Ignore negative paths
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Path passing through current node
            current_path = node.val + left + right

            self.ans = max(self.ans, current_path)

            # Return one-side path
            return node.val + max(left, right)

        dfs(root)

        return self.ans