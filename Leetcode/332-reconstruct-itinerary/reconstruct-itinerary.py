import heapq

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        graph = {}

        # Min-heap for lexical order
        for src, dst in tickets:

            if src not in graph:
                graph[src] = []

            heapq.heappush(graph[src], dst)

        itinerary = []

        def dfs(airport):

            heap = graph.get(airport, [])

            while heap:

                next_airport = heapq.heappop(heap)

                dfs(next_airport)

            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]
        