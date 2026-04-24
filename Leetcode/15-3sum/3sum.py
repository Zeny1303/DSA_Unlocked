class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = sorted(nums)
        # n = [-4,-1,-1,0,1,2]
        for i in range(len(n)-2):
            # duplicate nhi ane chahiye
            if i>0 and n[i] == n[i-1]:
                continue
            j=i+1
            k = len(n)-1
            while j<k:
                s = n[j]+n[k] + n[i]
                if s == 0:
                    res.append([n[i], n[j], n[k]])
                    # move pointers and avoid duplicates 
                    while j<k and n[j] == n[j+1]:
                        j+=1
                    while j< k and n[k] == n[k-1]:
                        k-=1    
                    j+=1
                    k-=1
                elif s < 0:
                    j+=1
                else:
                    k-=1     
        return res               

                           


        





        