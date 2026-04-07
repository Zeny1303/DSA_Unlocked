class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        
        # Step 1: skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Step 2: count last word length
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length