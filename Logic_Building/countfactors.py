def countFactors (n):
        # code here
        from math import sqrt
        count=0
        for i in range(1,int(sqrt(n))+1):
            if n % i == 0:
                count+=1
                if n // i !=i:
                    count+=1
        return count
n=125
print(countFactors(n))