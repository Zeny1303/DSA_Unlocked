def Halloumi_Boxes(n, k, arr):
    sorted_arr = sorted(arr)
    if k == 1:
        return arr == sorted_arr
    return True


t = int(input())#Reads t -> Number of test cases
for _ in range(t):
    n, k = map(int, input().split())
    # input() → reads a line from input as a string for example "1 2 3"
    # .split() → splits the string into a list of tokens for example ["1", "2", "3"]
    #map(int, ...) → converts each token to an integer for example [1, 2, 3]
    arr = list(map(int, input().split()))
    
    if Halloumi_Boxes(n, k, arr):
        print("YES")
    else:
        print("NO")




    


        
        

      

