class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        checker={}
        for words in strs:
            sortedlist="".join(sorted(words))            
            if sortedlist not in checker:
                checker[sortedlist]=[]    
                checker[sortedlist].append(words)
            else:
                checker[sortedlist].append(words)
        return(checker.values())
            
           