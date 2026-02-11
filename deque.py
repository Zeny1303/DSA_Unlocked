from collections import deque
lst =deque()
# insertion takes place in this direction -------->
lst.append(100)
lst.append(200)
lst.append(300)
print(lst)

#aage append krta hai <-------------
lst.appendleft(1)
lst.append(2)
print(lst)
