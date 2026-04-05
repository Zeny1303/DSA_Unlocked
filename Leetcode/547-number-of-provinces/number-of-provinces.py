class Solution(object):
    def dfs(self, node, isConnected, visited):
        visited[node] = True
        
        for j in range(len(isConnected)):
            if isConnected[node][j] == 1 and not visited[j]:
                self.dfs(j, isConnected, visited)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                self.dfs(i, isConnected, visited)
                provinces += 1

        return provinces