class Solution:
    def isRectangleOverlap(self, r1: list[int], r2: list[int]) -> bool:
        x = sorted([(r1[0], "r1"), (r1[2], "r1"), (r2[0], "r2"), (r2[2], "r2")])
        y = sorted([(r1[1], "r1"), (r1[3], "r1"), (r2[1], "r2"), (r2[3], "r2")])
        
        print(y,x)
        print(x[0][1], x[1][1])
        if x[0][1] == x[1][1] or x[2][1] == x[3][1] or y[0][1] == y[1][1] or y[2][1] == y[3][1] or x[2][0] == x[1][0] or y[2][0] == y[1][0]:
            return False
        return True
                
sol=Solution()
rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
res = sol.isRectangleOverlap(rec1,rec2)
print(res)


