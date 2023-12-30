class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        l = [0]*numRows
        for i in range(numRows):
            l[i] = [1]*(i+1)
            for j in range(1, i//2 + 1):
                l[i][j] = l[i-1][j-1]+l[i-1][j]
                l[i][-j-1] = l[i][j]
        return l


sol = Solution()
numRows = 6
res = sol.generate(numRows)
print(res)

# s=[1,3]
# b=reversed(s[0:3//2]
# d.extend()
