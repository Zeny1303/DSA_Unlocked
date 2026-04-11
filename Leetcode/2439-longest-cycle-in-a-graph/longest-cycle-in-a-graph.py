class Solution(object):
    
    def dfs(self,cycleLen,node,visitedNodelist,currentPath,edges):
        cycleLen+=1
        currentPath[node] =cycleLen
        visitedNodelist[node] = 1
        nbr = edges[node]
        if nbr!=-1:
            if not visitedNodelist[nbr]:
                self.dfs(cycleLen,nbr,visitedNodelist,currentPath,edges)
            elif currentPath[nbr] !=0:
                currCycleLen = currentPath[node]-currentPath[nbr]+1
                self.longestCycleLen=max(self.longestCycleLen,currCycleLen)    
        currentPath[node] = 0        
    def longestCycle(self,edges):
        self.longestCycleLen=-1
        numofNodes = len(edges)
        visitedNodelist = [0]*numofNodes
        currentPath = [0]*numofNodes
        for i in range(numofNodes):
            if visitedNodelist[i] !=1:
                self.dfs(1,i,visitedNodelist,currentPath,edges)
        return self.longestCycleLen        
    