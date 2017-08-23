# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# https://codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
# by oz 

def solution(A):
    # write your code in Python 2.7
    total=0
    left=A[0]
    
    for i in range(1,len(A)):
        total+=A[i]
    
    min=abs(left-total)
    
    for i in range(1,len(A)-1):
        left+=A[i]
        total-=A[i]
        tmp=abs(left-total)
        if tmp < min:
            min=tmp
            
    return min
    