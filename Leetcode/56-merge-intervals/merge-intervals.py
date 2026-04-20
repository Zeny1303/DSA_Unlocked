class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort(key=lambda x: x[0])
        currentstart = intervals[0][0]
        currentend = intervals[0][1]
        for i in range(1,len(intervals)):
            nextstart = intervals[i][0]
            nextend = intervals[i][1]
            if nextstart <= currentend:
                # merge 
                currentstart = currentstart
                currentend = max(currentend,nextend)
            # condition not ful fill that means it is independent thing
            else:    
                res.append([currentstart,currentend]) 
                currentstart = nextstart
                currentend = nextend
        # ek last ka bacha rhe jayega toh 
        res.append([currentstart,currentend])
        return res           

        