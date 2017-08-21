# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/4-counting_elements/missing_integer/
# by oz

def solution(A):
    # write your code in Python 2.7
    max_val=max(A)
    if max_val <0:
        return 1
    
    vals=[0 for i in xrange(max_val+1)]
    
    for num in A:
        if num > 0:
            vals[num]=1
    
    for i in range(1, len(vals)):
        if vals[i]==0:
            return i
            
    return max_val+1