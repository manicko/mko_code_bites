# Just wanted to share my two favorite binary search templates to help with this problem as well as any similar ones:
# Template 1: Find max value of x such that f(x) is true

def binarySearchForMinVal(lower_bound, upper_bound):
    l, r = lower_bound, upper_bound
    while l < r:
        mid = (l + r)//2 #round down
        if feasible(mid):
            r = mid #check for possible smaller values that work
        else:
            l = mid + 1 #values smaller than or equal to mid do not work. Reduce search space to values greater than mid.
    return l
# Template 2: Find min value of x such that f(x) is true

def binarySearchForMaxVal(lower_bound, upper_bound):
    l, r = lower_bound, upper_bound
    while l < r:
        mid = (l + r + 1)//2 #round up
        if feasible(mid):
            l = mid #check for possible greater values that work
        else:
            r = mid - 1 #values greater than or equal to mid do not work. Reduce search space to values smaller than mid.
    return l