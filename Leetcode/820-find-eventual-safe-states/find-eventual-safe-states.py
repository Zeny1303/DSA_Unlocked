class Solution(object):
    # CYCLE DETECTION 
    def dfs(self,node, graph, visited, currentpath):
        visited[node] =1
        currentpath[node]=1
        for nbr in graph[node]:
            if not visited[nbr]:
                res = self.dfs(nbr,graph,visited,currentpath)
                if res:
                    return True
            else:
                if currentpath[nbr]==1:
                    # we have foud cycle
                    return True
        currentpath[node] =0
        return False            


    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n=len(graph)
        # step 1 - creating a g 
        
        visited =[0]*n
        currentpath =[0]*n
        r=[]
        for i in range(n):
            if not visited[i]:
                self.dfs(i,graph,visited,currentpath)
        for i in range(n):
            if currentpath[i]==0:
                r.append(i)
        return r        