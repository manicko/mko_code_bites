'''766. Toeplitz Matrix
https://leetcode.com/problems/toeplitz-matrix/
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:

    In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

matrix = [[1,2,3,4],
          [5,1,2,3],
          [9,5,1,2],
          [7,9,5,1],          
          [6,7,9,5],  
          [8,6,7,9]]


'''

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == n == 1: return True
        # T_flag = True
        # print("m=",m,"n=",n)
        for i in range(-m,n):
            flag = True
            # if T_flag == False: break
            for el in zip(matrix):        
                if 0 <= i < n:
                    # print(el[0][i])
                    if flag: 
                         check = el[0][i]
                         flag = False
                    elif check != el[0][i]:                  
                        return False
                        break          
                elif i >= n: break
                i += 1
            # print('next loop')
        return True
    

matrix = [[1,2,3,4],                
          [6,7,9,5],  
          [8,6,7,9]]


s = Solution()
test = s.isToeplitzMatrix(matrix)

print(test)
        
      
        
       