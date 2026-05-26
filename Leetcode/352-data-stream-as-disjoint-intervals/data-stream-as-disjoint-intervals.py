class SummaryRanges(object):

    def __init__(self):

        self.nums = set()

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """

        self.nums.add(value)

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """

        if not self.nums:
            return []

        nums = sorted(self.nums)

        intervals = []

        start = nums[0]
        end = nums[0]

        for i in range(1, len(nums)):

            # Consecutive number
            if nums[i] == end + 1:

                end = nums[i]

            else:

                intervals.append([start, end])

                start = nums[i]
                end = nums[i]

        intervals.append([start, end])

        return intervals