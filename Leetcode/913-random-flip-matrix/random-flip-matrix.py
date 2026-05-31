import random

class Solution(object):

    def __init__(self, m, n):
        """
        :type m: int
        :type n: int
        """
        self.rows = m
        self.cols = n
        self.total = m * n
        self.map = {}

    def flip(self):
        """
        :rtype: List[int]
        """
        r = random.randint(0, self.total - 1)

        self.total -= 1

        x = self.map.get(r, r)

        self.map[r] = self.map.get(self.total, self.total)

        return [x // self.cols, x % self.cols]

    def reset(self):
        """
        :rtype: None
        """
        self.map.clear()
        self.total = self.rows * self.cols