class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        k = len(primes)

        ugly = [1] * n

        pointers = [0] * k

        values = primes[:]

        for i in range(1, n):

            next_ugly = min(values)

            ugly[i] = next_ugly

            # Update all matching pointers
            for j in range(k):

                if values[j] == next_ugly:

                    pointers[j] += 1

                    values[j] = ugly[pointers[j]] * primes[j]

        return ugly[-1]