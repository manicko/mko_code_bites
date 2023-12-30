# put your python code here
n = int(input())
nums = [1] * (n + 1)
for i in range(0, n + 1):
    nums[i] = [1] * (i + 1)
    for j in range(1, i):
        nums[i][j] = nums[i - 1][j - 1] + nums[i - 1][j]
print(nums[-1])
