"""
Extracting last digits of a number
"""
Number = 12345
while Number >0:
    Last_Digit = Number % 10
    print(Last_Digit)
    Number = Number // 10
    print(Number)