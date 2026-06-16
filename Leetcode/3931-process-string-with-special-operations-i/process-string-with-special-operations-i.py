class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for char in s :
            if 'a' <= char <= 'z': # Append char
                ans = char
                result += ans
            elif char == "#": # Duplicate result
                result = result * 2
            elif char == "%": # Reverse result
                result = result[::-1]
            elif char == "*": # Remove the last character
                result = result[:-1]    
        return result         



        