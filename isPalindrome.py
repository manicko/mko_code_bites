'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

best solution:
def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

Follow up: Could you solve it without converting the integer to a string?


'''


class Solution:
    def isValid(self, s: str) -> bool:        
        dict = ('()','{}','[]')
        a = len(s) + 1
        while len(s) < a:
            a = len(s)
            for w in dict:
                # print(w)
                s = s.replace(w,'')
        if len(s): return False
        else: return True
        
          
# s='[[[(){}[{}({()[]{}{{}}})(){}]]([)]]]'
# s = "(]"
s = "()[]{}"
# [[[(){}[{}({()[]{}{{}}})(){}]]]]
# [[[(){}[{}({()[]{}{{}}})(){}]]]]
sol = Solution()
test = sol.isValid(s)

print(test)
        
      
        
       