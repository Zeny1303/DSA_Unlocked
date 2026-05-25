# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        heap = []

        # Push first node of each list into heap
        for i in range(len(lists)):

            if lists[i]:

                # (node value, index, node)
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        current = dummy

        while heap:

            val, i, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            # Push next node from same list
            if node.next:

                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next