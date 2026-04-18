class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mp1 ={}
        mp2 ={}
        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]
            if ch1 in mp1 and mp1[ch1] != ch2 or ch2 in mp2 and mp2[ch2]!=ch1:
                return False
            # map krege 
            mp1[ch1] = ch2
            mp2[ch2] = ch1
        return True     
        
                
            
        