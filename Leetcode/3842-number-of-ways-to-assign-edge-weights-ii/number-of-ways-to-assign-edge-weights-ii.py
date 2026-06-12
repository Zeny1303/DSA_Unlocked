from typing import List
import sys

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        sys.setrecursionlimit(1 << 25)

        n = len(edges) + 1
        LOG = 17

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        parent = [[-1] * (n + 1) for _ in range(LOG)]

        def dfs(u, p):
            parent[0][u] = p
            for v in graph[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    dfs(v, u)

        dfs(1, -1)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                if parent[k - 1][v] != -1:
                    parent[k][v] = parent[k - 1][parent[k - 1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            a = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[a]
            ans.append(pow(2, dist - 1, MOD))

        return ans