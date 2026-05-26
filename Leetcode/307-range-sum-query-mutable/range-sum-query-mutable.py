class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.n = len(nums)

        # Fenwick Tree
        self.bit = [0] * (self.n + 1)

        self.nums = nums[:]

        for i in range(self.n):
            self._add(i + 1, nums[i])

    def _add(self, index, value):

        while index <= self.n:

            self.bit[index] += value

            index += index & -index

    def _prefix_sum(self, index):

        total = 0

        while index > 0:

            total += self.bit[index]

            index -= index & -index

        return total

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        delta = val - self.nums[index]

        self.nums[index] = val

        self._add(index + 1, delta)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        return self._prefix_sum(right + 1) - self._prefix_sum(left)