"""
Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.
 
Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]

Example 5:

Input: num = "3456237490", target = 9191
Output: []
 
Constraints:

1 <= num.length <= 10
num consists of only digits.
-2^31 <= target <= 2^31 - 1
"""

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        def backtrack(i, path, temp, prev):
            if i == len(num):
                if temp == target:
                    res.append(path)
                return
            
            for j in range (i, len(num)):
                if j > i and num[i] =='0':
                    break
                num1 = int(num[i:j + 1])
                if i == 0:
                    backtrack(j + 1, path + str(num1), temp + num1, num1)
                else:
                    backtrack(j + 1, path + "+" + str(num1), temp + num1, num1)
                    backtrack(j + 1, path + "-" + str(num1), temp - num1, -num1)
                    backtrack(j + 1, path + "*" + str(num1), temp - prev + prev * num1, prev * num1)
        
        res = []
        backtrack(0, "", 0, 0)
        return res;
