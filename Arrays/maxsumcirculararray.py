# 918. Maximum Sum Circular Subarray
def maxSubarraySumCircular(nums):
    n=len(nums)
    def kadane_algorithm(nums):
        total=0
        sum_from_kadane=0
        maxi=float('-inf')
        for i in range(0,n):
            total = total+nums[i]
            maxi=max(total,maxi)
            if total<0:
                total = 0
        return maxi

    def rotate_array(nums):
        temp = nums[n-1] 
        for i in range(n-2,-1,-1):
            nums[i+1]= nums[i]
        nums[0] = temp
    result =0
    for i in range(0,n):
        # if current array
        rotate_array(nums)
        sum = kadane_algorithm(nums)
        result = max(sum,result)
    return result   

nums = [5,-3,5]
answer = maxSubarraySumCircular(nums)
print(answer)         

