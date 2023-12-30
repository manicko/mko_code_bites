# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:43:44 2022

@author: NMatveichev

Given a roman numeral, convert it to an integer.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""
class Solution:
    def romanToInt(self, s: str) -> int:      
        r_dict = {
                    'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000    
                    }
        b = 0          
        i = 0
        a = 0
        
        while i < len(s) -1:
            n_cur = int(r_dict[s[i]])
            n_next = int(r_dict[s[i+1]])
            print ('s=',s[i],s[i+1])
            if n_cur > n_next:
                a += n_cur + b
                b = 0
            elif n_cur < n_next:
                a = a - n_cur - b
                b = 0
            elif n_cur == n_next: 
                b += n_cur
            i +=1    
        a = a + b + r_dict[s[-1]] 
        
        return a
 
s1 = Solution()
    
r_str = str(input("Введите римское число: "))
res = s1.romanToInt(s=r_str)
print ("Римское {0} = {1}".format(r_str,res))
