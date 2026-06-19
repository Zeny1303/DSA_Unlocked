class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt =[0]
        
        for i in range(len(gain)):
            next_alt = gain[i]+alt[i]
            alt.append(next_alt)
        return max(alt)    

    