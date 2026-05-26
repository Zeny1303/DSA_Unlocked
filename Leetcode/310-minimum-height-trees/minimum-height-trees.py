from collections import defaultdict, deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        # Build graph
        for u, v in edges:

            graph[u].append(v)
            graph[v].append(u)

            degree[u] += 1
            degree[v] += 1

        # Initial leaves
        leaves = deque()

        for i in range(n):

            if degree[i] == 1:
                leaves.append(i)

        remaining_nodes = n

        # Remove leaves layer by layer
        while remaining_nodes > 2:

            leaf_count = len(leaves)

            remaining_nodes -= leaf_count

            for _ in range(leaf_count):

                leaf = leaves.popleft()

                for neighbor in graph[leaf]:

                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)