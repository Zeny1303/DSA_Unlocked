class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        freq = {}

        def dfs(node):
            if not node:
                return 0

            total = node.val + dfs(node.left) + dfs(node.right)

            freq[total] = freq.get(total, 0) + 1

            return total

        dfs(root)

        max_freq = max(freq.values())

        return [s for s, count in freq.items() if count == max_freq]