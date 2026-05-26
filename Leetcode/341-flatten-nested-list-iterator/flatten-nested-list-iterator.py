class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """

        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """

        while self.stack:

            top = self.stack[-1]

            # Integer found
            if top.isInteger():
                return True

            # Expand nested list
            self.stack.pop()

            nested = top.getList()

            self.stack.extend(nested[::-1])

        return False