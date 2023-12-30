import heapq
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        heap, ans, = [], [] 
        for s, e in intervals + [newInterval]: # add start & end to heap (-1 is start, 1 is end)
            heapq.heappush(heap, (s, -1))
            heapq.heappush(heap, (e, 1))
        cur, s = 0, None            
        while heap:                            
            i, val = heapq.heappop(heap)       # pop heap
            if s is None: s = i                # is s is None, assign i to s (interval start)
            cur += val                         # keep counting until close interval
            if not cur:                        # when cur == 0, meaning we can close the interval
                ans.append([s, i])             # append interval to ans
                s = None                       # reset s to None
        return ans        

sol=Solution()
ntervals = [[7,15],[25,35],[45,55],[65,75],[80,100]]
newInterval = [26,55]
res = sol.insert(ntervals,newInterval)
print(res)


#[1,0,0,2,3,0,0,4]