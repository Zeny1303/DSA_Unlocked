class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        f = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            f[sorted_word].append(word)

        return list(f.values())    
        