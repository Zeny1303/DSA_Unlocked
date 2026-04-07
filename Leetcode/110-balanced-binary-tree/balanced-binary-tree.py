class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node) -> int:
            if not node:
                return 0

            left_h = height(node.left)
            if left_h == -1:            # imbalance already found below
                return -1

            right_h = height(node.right)
            if right_h == -1:           # imbalance already found below
                return -1

            if abs(left_h - right_h) > 1:   # imbalance at current node
                return -1

            return 1 + max(left_h, right_h) # valid height

        return height(root) != -1