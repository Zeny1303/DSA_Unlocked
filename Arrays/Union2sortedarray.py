#Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.
#Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.

#Examples:

#Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
#Output: [1, 2, 3, 4, 5, 6, 7]
#Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.


def union2sortedarray(a,b):
    result = []
    j,i=0,0
    while i < len(a) and j < len(b):
        if a[i] ==b[j]:
            result.append(a[i])
            i+=1
            j+=1
        elif a[i]>b[j]:
            result.append(b[j])
            j+=1
        elif a[i]<b[j]:
            result.append(a[i])
            i+=1
    if i < len(a):
        while i<len(a):
            result.append(a[i])
            i+=1
    if j < len(b):
        while j < len(b):
            result.append(b[j])
            j+=1        

    return result

a=[1,2,3,4,5] 
b=[1,2,3,6,7]
answer = union2sortedarray(a,b)
print(answer)    

