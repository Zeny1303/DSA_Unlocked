class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        n = len(machines)

        if total % n != 0:
            return -1

        target = total // n

        moves = 0
        balance = 0

        for dresses in machines:
            diff = dresses - target
            balance += diff

            moves = max(
                moves,
                abs(balance),
                diff
            )

        return moves