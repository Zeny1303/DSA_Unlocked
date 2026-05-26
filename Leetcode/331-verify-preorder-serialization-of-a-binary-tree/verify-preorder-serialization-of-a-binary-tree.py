class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        slots = 1

        nodes = preorder.split(',')

        for node in nodes:

            # Consume one slot
            slots -= 1

            # No slot available
            if slots < 0:
                return False

            # Non-null node creates two new slots
            if node != '#':
                slots += 2

        return slots == 0