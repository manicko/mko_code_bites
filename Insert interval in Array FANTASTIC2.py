import bisect
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        ''' 
        1) Solve border conditions: 
        left border of newInterval is to the right of intervals 
        and vice versa
        2) Find indices to position newInterval left and right values in intervals
        using binary search func bisect
        3) Correct indices to exact inteval
        4) Solve border conditions if between intervals
        5) Update intervals 
        '''
        
        left, right = newInterval
        
        if len(intervals) ==0 or intervals[-1][-1] < left:
            intervals.append(newInterval)
            return intervals 
        
        if intervals[0][0] > right:
            intervals = [newInterval] + intervals
            return intervals
        
        #Find indices by comparing leftmost and rightmost values of both arrays'
        idx_left = bisect.bisect_left(intervals, left, key=lambda x: x[0])
        idx_right = bisect.bisect_left(intervals, right, key=lambda x: x[0])
       
       # print(idx_left,idx_right)
        
        #Correct indices to exact inteval'
        if idx_left > 0 and intervals[idx_left -1][0] <= left <= intervals[idx_left -1][1]: 
            idx_left -= 1
            
        if idx_right > len(intervals) -1:
            idx_right = len(intervals) -1
        if idx_right > 0 and intervals[idx_right -1][0] <= right < intervals[idx_right][0]: 
            idx_right -= 1
        # print(idx_left,idx_right)     
        left0, left1 = intervals[idx_left]
        right0, right1 = intervals[idx_right]
            
        # print(idx_left,idx_right)
        # print(left0, left1,left)
        # print(right0, right1,right)
            
        # interval somewhere in between
        #border conditions if between intervals'
        if idx_left == idx_right and left1 < left:
            intervals.insert(idx_left+1, newInterval)
            return intervals        
        else:
            #ordinary case'
            left = min(left,left0)
            right = max(right,right1)
            intervals = intervals[:idx_left]+[[left,right]]+intervals[idx_right+1:]
                
        return intervals

sol=Solution()
ntervals = [[1,5]]
newInterval = [2,3]
res = sol.insert(ntervals,newInterval)
print(res)


#[1,0,0,2,3,0,0,4]