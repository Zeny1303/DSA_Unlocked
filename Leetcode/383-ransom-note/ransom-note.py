class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        # check krna hai ki magazine mein ramsom Note ke letter  hai ki nhi 
        # freq map bano magazine ke liye 
        m ={}
        for ch in magazine:
            m[ch]= m.get(ch,0)+1
        # abh hum freq map iterate krege 
        for ch in ransomNote:
            if m.get(ch,0) == 0:
                # character ka freq 0 hogye mtb simple baad woh letter abh nhia hai
                return False
            m[ch]-=1    
        return True
