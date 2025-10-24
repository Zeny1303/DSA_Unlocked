def isArmstrong(num):
    # Write your code here.5
    42
    number = num 
    answer = 0
    nod = len(str(number))
    print(nod)
    while number >0:
        digits = number %10
        answer = answer + (digits ** nod)
        number = number // 10
    if answer == num :
        return True
    else :
        return False  
    
num = 153
if isArmstrong(num):
    print("Yes")
else:
    print("No")    