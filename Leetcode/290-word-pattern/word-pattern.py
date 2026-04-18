class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
    
        # p -> s and s -> p
        mp1 ={}
        mp2={}
        words = s.split()
        if len(pattern) != len(words):
            return False
            

        for i in range(len(pattern)):
            ch1 = pattern[i] # a
            ch2 = words[i] # dog

            if ch1 in mp1 and mp1[ch1]!=ch2 or ch2 in mp2 and mp2[ch2]!=ch1:
                return False

            mp1[ch1] = ch2
            mp2[ch2] = ch1
        return True     


        