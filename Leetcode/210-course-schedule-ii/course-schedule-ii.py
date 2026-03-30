from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        # directed graph
        graph = [[] for _ in range(n)]
        for u,v in prerequisites:
            graph[v].append(u)
        # indegree calculations
        indegree =[0]*n
        for i in range(n):
            for x in graph[i]:
                indegree[x]+=1
        # queue
        q=deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        ans =[]
        # kahn's algorithm 
        while q:
            f=q.popleft()
            ans.append(f)
            for x in graph[f]:
                indegree[x]-=1
                if indegree[x]==0:
                    q.append(x)
        if len(ans) != n:
            return []
        return ans                         


        