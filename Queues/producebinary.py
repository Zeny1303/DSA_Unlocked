### Produce Binary Number from 1 to 10


from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()
    def enqueue(self,val):
        return self.container.appendleft(val)
        # self.container.append(val)
        # self.container.insert(0,val)
    def dequeue(self):
        return self.container.pop()#for appendleft or insert
        #self.container.popleft()
    def is_Empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
    def front(self):
        return self.container[-1]
def producebinary(n):
        q=Queue()
        q.enqueue("1")
        for i in range(n):
            front=q.front()
            print(front,end=" ")
            q.enqueue(front+"0")
            q.enqueue(front+"1")
            q.dequeue()
n=10
result=producebinary(n)